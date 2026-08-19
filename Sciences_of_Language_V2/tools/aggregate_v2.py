#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import os
import shutil
import subprocess
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from xml.sax.saxutils import escape

SOURCES = [
    ("001_MEM_U_ZIN", "Mem û Zîn", "Classical poetic/literary source"),
    ("002_ANHA", "ANHA", "Modern news source"),
    ("003_RONAHI", "Ronahî", "Modern broadcast/news source"),
    ("004_RUDAW", "Rudaw", "Modern news/opinion source"),
    ("005_PIRTUKEN_KURMANCI_KATALOG", "Pirtûkên Kurmancî Katalog", "Book/catalog source"),
    ("006_KURMANJI_BEGINNERS", "Kurmanji Beginners", "Pedagogical source"),
    ("007_KOVARA_KURMANCI", "Kovara Kurmancî", "Periodical source"),
    ("008_KOVARA_HAWAR", "Kovara Hawar", "Historical periodical source"),
    ("009_ROJNAMA_KURDISTAN", "Rojnama Kurdistan", "Historical newspaper source"),
    ("010_KOVARA_JIN", "Kovara Jîn", "Historical periodical source"),
    ("011_FOLKLORA_KURMANCA_1936", "Folklora Kurmanca (1936)", "Folklore source"),
    ("012_KURD_TEAVUN_TERAKKI_1908", "Kurd Teavun Terakki (1908)", "Historical journal source"),
    ("013_ROJI_KURD_1913", "Rojî Kurd (1913)", "Historical periodical source"),
    ("014_DIROK_U_CIVAKA_KURDAN", "Dîrok û Civaka Kurdan", "Monograph/research source"),
]
DISPLAY = {f:n for f,n,_ in SOURCES}
DOMAIN = {f:d for f,_,d in SOURCES}
N_SOURCES = len(SOURCES)
KINDS = ["BIGRAMS","TRIGRAMS","FOURGRAMS","SLOT_FRAMES","GAP2","GAP3"]


def entropy_norm(counter: Counter) -> float:
    vals=[v for v in counter.values() if v>0]
    if len(vals)<=1: return 0.0
    total=sum(vals)
    h=-sum((v/total)*math.log(v/total) for v in vals)
    return h/math.log(len(vals))


def gz_rows(path: Path):
    with gzip.open(path,"rt",encoding="utf-8",newline="") as f:
        yield from csv.DictReader(f,delimiter="\t")


def write_gz_tsv(path: Path, fields, rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with gzip.open(path,"wt",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",extrasaction="ignore")
        w.writeheader(); w.writerows(rows)


def write_tsv(path: Path, fields, rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",extrasaction="ignore")
        w.writeheader(); w.writerows(rows)


def pattern_key(kind: str, r: dict):
    if kind=="BIGRAMS": return (r["form_1"],r["form_2"])
    if kind=="TRIGRAMS": return (r["form_1"],r["form_2"],r["form_3"])
    if kind=="FOURGRAMS": return (r["form_1"],r["form_2"],r["form_3"],r["form_4"])
    if kind in {"GAP2","GAP3"}: return (r["left_form"],r["right_form"])
    if kind=="SLOT_FRAMES": return (r["left_form"],r["right_form"])
    raise ValueError(kind)


def complexity_value(kind: str, extra: dict|None=None):
    if kind=="BIGRAMS": return .35
    if kind=="TRIGRAMS": return .60
    if kind=="FOURGRAMS": return .80
    if kind=="GAP2": return .50
    if kind=="GAP3": return .60
    if kind=="SLOT_FRAMES":
        d=int((extra or {}).get("fillers_sum",0))
        return min(1.0, math.log1p(d)/math.log(51)) if d>0 else .45
    return .4


def aggregate_kind(artifacts: Path, out: Path, kind: str):
    # The per-source retained tables may collectively contain millions of rows.
    # Use an external-sort spool keyed by a JSON tuple to keep aggregation bounded.
    with tempfile.TemporaryDirectory(prefix=f"tslk_v2_{kind.lower()}_") as td:
        td=Path(td); spool=td/"spool.tsv"; sortedp=td/"sorted.tsv"; rawagg=td/"agg.jsonl"
        source_row_counts={}
        with spool.open("w",encoding="utf-8",newline="") as sf:
            for folder,_,_ in SOURCES:
                p=artifacts/"Per_Source"/folder/"Patterns"/f"{kind}.tsv.gz"
                if not p.exists(): raise SystemExit(f"Missing {p}")
                n=0
                for r in gz_rows(p):
                    n+=1
                    key=json.dumps(pattern_key(kind,r),ensure_ascii=False,separators=(",",":"))
                    support=int(r.get("support") or r.get("total_support") or 0)
                    if kind=="SLOT_FRAMES":
                        extras=json.dumps({"distinct_fillers":int(r.get("distinct_fillers",0) or 0),"filler_entropy":float(r.get("filler_entropy",0) or 0)},separators=(",",":"))
                    else: extras="{}"
                    sf.write(f"{key}\t{folder}\t{support}\t{extras}\n")
                source_row_counts[folder]=n
        env=os.environ.copy(); env["LC_ALL"]="C"
        with sortedp.open("wb") as o:
            subprocess.run(["sort","-t","\t","-k1,1",str(spool)],stdout=o,check=True,env=env)

        max_support=1; cross_rows=0
        with sortedp.open("r",encoding="utf-8") as f, rawagg.open("w",encoding="utf-8") as o:
            current=None; counts=Counter(); fillers_sum=0; ent_weight=0.0; ent_weight_n=0
            def flush():
                nonlocal current,counts,fillers_sum,ent_weight,ent_weight_n,max_support,cross_rows
                if current is None or len(counts)<2: return
                total=sum(counts.values()); max_support=max(max_support,total); cross_rows+=1
                rec={"key":json.loads(current),"source_support":dict(counts),"total_support":total,"source_count":len(counts),"source_entropy":entropy_norm(counts)}
                if kind=="SLOT_FRAMES":
                    rec["fillers_sum"]=fillers_sum
                    rec["mean_source_filler_entropy"]=(ent_weight/ent_weight_n if ent_weight_n else 0.0)
                o.write(json.dumps(rec,ensure_ascii=False,separators=(",",":"))+"\n")
            for line in f:
                key,folder,supp,extras=line.rstrip("\n").split("\t",3)
                if current is not None and key!=current:
                    flush(); counts=Counter(); fillers_sum=0; ent_weight=0.0; ent_weight_n=0
                current=key; s=int(supp); counts[folder]+=s
                if kind=="SLOT_FRAMES":
                    ex=json.loads(extras); fillers_sum += int(ex.get("distinct_fillers",0)); ent=float(ex.get("filler_entropy",0)); ent_weight += ent*s; ent_weight_n += s
            flush()

        fields=["pattern_id","kind","source_count","sources","aggregate_support","source_entropy","complexity_component","construction_evidence_score","status"]
        if kind in {"BIGRAMS","GAP2","GAP3"}: fields[2:2]=["form_1","form_2"]
        elif kind=="TRIGRAMS": fields[2:2]=["form_1","form_2","form_3"]
        elif kind=="FOURGRAMS": fields[2:2]=["form_1","form_2","form_3","form_4"]
        elif kind=="SLOT_FRAMES": fields[2:2]=["left_form","right_form","source_local_distinct_fillers_sum","mean_source_filler_entropy"]

        scored=[]
        with rawagg.open("r",encoding="utf-8") as f:
            for i,line in enumerate(f,1):
                r=json.loads(line); sc=r["source_count"]; total=r["total_support"]; ent=r["source_entropy"]
                comp=complexity_value(kind,r)
                score=100*(.35*(sc/N_SOURCES)+.30*(math.log1p(total)/math.log1p(max_support))+.20*ent+.15*comp)
                key=r["key"]
                row={"pattern_id":f"{kind[:4]}-{i:09d}","kind":kind,"source_count":sc,"sources":" | ".join(DISPLAY[x] for x in sorted(r["source_support"])),"aggregate_support":total,"source_entropy":f"{ent:.8f}","complexity_component":f"{comp:.8f}","construction_evidence_score":f"{score:.4f}","status":"CROSS-SOURCE STRUCTURAL CANDIDATE / FUNCTION UNRESOLVED"}
                if kind in {"BIGRAMS","GAP2","GAP3"}: row.update({"form_1":key[0],"form_2":key[1]})
                elif kind=="TRIGRAMS": row.update({f"form_{j+1}":x for j,x in enumerate(key)})
                elif kind=="FOURGRAMS": row.update({f"form_{j+1}":x for j,x in enumerate(key)})
                elif kind=="SLOT_FRAMES": row.update({"left_form":key[0],"right_form":key[1],"source_local_distinct_fillers_sum":r.get("fillers_sum",0),"mean_source_filler_entropy":f"{r.get('mean_source_filler_entropy',0):.8f}"})
                scored.append(row)
        scored.sort(key=lambda r:(-float(r["construction_evidence_score"]),-r["source_count"],-r["aggregate_support"]))
        write_gz_tsv(out/"Data"/f"CROSS_SOURCE_{kind}.tsv.gz",fields,scored)
        return {"kind":kind,"cross_source_rows":len(scored),"source_retained_rows":source_row_counts,"top":scored[:50]}


def aggregate_morphology(artifacts: Path, out: Path):
    acc={}
    for folder,_,_ in SOURCES:
        p=artifacts/"Per_Source"/folder/"MORPH_CONTEXT_PAIR_EVIDENCE.tsv.gz"
        if not p.exists(): raise SystemExit(f"Missing {p}")
        for r in gz_rows(p):
            key=(r["base_form"],r["extended_form"],r["edge_side"],r["added_edge_material"])
            x=acc.setdefault(key,{"support":Counter(),"ctx_num":0.0,"ctx_den":0,"v1":r.get("v1_score","")})
            s=min(int(r["base_frequency"]),int(r["extended_frequency"])); sim=float(r["combined_context_similarity"])
            x["support"][folder]+=s; x["ctx_num"] += sim*s; x["ctx_den"] += s
    maxsupp=max((sum(x["support"].values()) for x in acc.values() if len(x["support"])>=2),default=1)
    rows=[]
    for key,x in acc.items():
        if len(x["support"])<2: continue
        total=sum(x["support"].values()); sim=x["ctx_num"]/x["ctx_den"] if x["ctx_den"] else 0; ent=entropy_norm(x["support"]); sc=len(x["support"])
        score=100*(.35*(sc/N_SOURCES)+.25*(math.log1p(total)/math.log1p(maxsupp))+.30*sim+.10*ent)
        rows.append({"base_form":key[0],"extended_form":key[1],"edge_side":key[2],"added_edge_material":key[3],"source_count":sc,"sources":" | ".join(DISPLAY[s] for s in sorted(x["support"])),"aggregate_min_frequency_support":total,"source_entropy":f"{ent:.8f}","mean_full_context_similarity":f"{sim:.8f}","v1_score":x["v1"],"morphology_context_evidence_score_v2":f"{score:.4f}","status":"V1 FORM-FAMILY CANDIDATE / V2 FULL-CONTEXT CROSS-SOURCE TEST / FUNCTION UNRESOLVED"})
    rows.sort(key=lambda r:(-float(r["morphology_context_evidence_score_v2"]),-r["source_count"],-r["aggregate_min_frequency_support"]))
    fields=list(rows[0]) if rows else ["base_form"]
    write_gz_tsv(out/"Data"/"MORPHOLOGY_CONTEXT_VALIDATION_V2.tsv.gz",fields,rows)
    return rows


def aggregate_positions(artifacts: Path, out: Path):
    acc={}
    for folder,_,_ in SOURCES:
        p=artifacts/"Per_Source"/folder/"POSITION_PROFILES.tsv.gz"
        for r in gz_rows(p):
            form=r["surface_form"]
            x=acc.setdefault(form,{"sources":set(),"freq":0,"initial":0,"final":0,"dec":[0]*10})
            x["sources"].add(folder); x["freq"]+=int(r["frequency"]); x["initial"]+=int(r["initial_count"]); x["final"]+=int(r["final_count"])
            for i in range(10): x["dec"][i]+=int(r[f"decile_{i}"])
    rows=[]
    for form,x in acc.items():
        if len(x["sources"])<2: continue
        r={"surface_form":form,"source_count":len(x["sources"]),"sources":" | ".join(DISPLAY[s] for s in sorted(x["sources"])),"frequency":x["freq"],"initial_count":x["initial"],"final_count":x["final"]}
        for i,v in enumerate(x["dec"]): r[f"decile_{i}"]=v
        rows.append(r)
    rows.sort(key=lambda r:(-r["source_count"],-r["frequency"],r["surface_form"].casefold(),r["surface_form"]))
    fields=list(rows[0]) if rows else ["surface_form"]
    write_gz_tsv(out/"Data"/"CROSS_SOURCE_POSITION_PROFILES.tsv.gz",fields,rows)
    return rows


def read_audits(artifacts: Path):
    rows=[]
    for folder,name,domain in SOURCES:
        p=artifacts/"Per_Source"/folder/"CORPUS_AUDIT.json"
        if not p.exists(): raise SystemExit(f"Missing {p}")
        a=json.loads(p.read_text(encoding="utf-8"))
        if not a.get("coverage_pass"): raise SystemExit(f"Coverage failed: {folder}")
        a["source"]=name; a["domain"]=domain; rows.append(a)
    return rows


def copy_compact_per_source(artifacts: Path, out: Path, pattern_results: dict):
    # Commit audits, full position/morphology validation tables, and compact top-pattern tables.
    # Full per-source recurrent sequence tables remain deterministic build artifacts; aggregate cross-source tables are repository-resident.
    for folder,_,_ in SOURCES:
        src=artifacts/"Per_Source"/folder; dst=out/"Per_Source"/folder; dst.mkdir(parents=True,exist_ok=True)
        for name in ["CORPUS_AUDIT.json","POSITION_PROFILES.tsv.gz","MORPH_CONTEXT_PAIR_EVIDENCE.tsv.gz"]:
            shutil.copy2(src/name,dst/name)
        pdir=dst/"Top_Patterns"; pdir.mkdir(exist_ok=True)
        for kind in KINDS:
            p=src/"Patterns"/f"{kind}.tsv.gz"
            rows=[]
            for i,r in enumerate(gz_rows(p)):
                if i>=5000: break
                rows.append(r)
            if rows:
                write_gz_tsv(pdir/f"TOP_{kind}.tsv.gz",list(rows[0]),rows)


def graph_v2(out: Path, pattern_results: dict, morph_rows, max_each=20000):
    graph=out/"Graph"; graph.mkdir(parents=True,exist_ok=True)
    nodes={}; edges=[]
    def node(nid,typ,label): nodes[nid]=(typ,label)
    for folder,name,_ in SOURCES: node(f"SRC:{folder}","SOURCE",name)
    for kind,res in pattern_results.items():
        for r in res["top"][:max_each]:
            pid=f"PAT:{kind}:{r['pattern_id']}"; node(pid,"PATTERN",r["pattern_id"])
            for src in r["sources"].split(" | "):
                folder=next((f for f,n,_ in SOURCES if n==src),None)
                if folder: edges.append((f"SRC:{folder}",pid,"SOURCE_ATTESTS_PATTERN",r["aggregate_support"],r["construction_evidence_score"]))
            forms=[]
            for k,v in r.items():
                if k.startswith("form_") or k in {"left_form","right_form"}: forms.append(v)
            for form in dict.fromkeys(forms):
                fid="FORM:"+form; node(fid,"FORM",form); edges.append((pid,fid,"PATTERN_CONTAINS_FORM",r["aggregate_support"],r["construction_evidence_score"]))
    for i,r in enumerate(morph_rows[:50000],1):
        mid=f"MORPH:{i:08d}"; node(mid,"FORM_FAMILY_CANDIDATE",f"{r['base_form']} ↔ {r['extended_form']}")
        for form,etype in [(r["base_form"],"FAMILY_BASE_FORM"),(r["extended_form"],"FAMILY_EXTENDED_FORM")]:
            fid="FORM:"+form; node(fid,"FORM",form); edges.append((mid,fid,etype,r["aggregate_min_frequency_support"],r["morphology_context_evidence_score_v2"]))
    write_gz_tsv(graph/"LANGUAGE_GRAPH_V2_NODES.tsv.gz",["node_id","node_type","label"],({"node_id":k,"node_type":v[0],"label":v[1]} for k,v in sorted(nodes.items())))
    write_gz_tsv(graph/"LANGUAGE_GRAPH_V2_EDGES.tsv.gz",["from_node","to_node","edge_type","support","evidence_score"],({"from_node":a,"to_node":b,"edge_type":t,"support":s,"evidence_score":e} for a,b,t,s,e in edges))
    # Compact GraphML: node/edge types only; evidence tables remain authoritative.
    with gzip.open(graph/"LANGUAGE_GRAPH_V2_CORE.graphml.gz","wt",encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns">\n')
        f.write('<key id="nt" for="node" attr.name="type" attr.type="string"/>\n<key id="et" for="edge" attr.name="type" attr.type="string"/>\n<graph id="TSLK-V2" edgedefault="directed">\n')
        for nid,(typ,label) in nodes.items(): f.write(f'<node id="{escape(nid)}"><data key="nt">{escape(typ)}</data></node>\n')
        for i,(a,b,t,_,_) in enumerate(edges): f.write(f'<edge id="e{i}" source="{escape(a)}" target="{escape(b)}"><data key="et">{escape(t)}</data></edge>\n')
        f.write('</graph></graphml>\n')
    return len(nodes),len(edges)


def report(out: Path, audits, pattern_results, morph_rows, pos_rows, graph_counts):
    lines=[
        "# Kurdish-TSL — Sciences of Language Full-Occurrence Structural Reconstruction V2","",
        "## Scientific status","",
        "**FULL OCCURRENCE STREAM SCANNED / STRUCTURAL CANDIDATES DISCOVERED / CONVENTIONAL GRAMMAR NOT YET ASSIGNED**","",
        "V2 reads every committed Deep Dictionary occurrence row and reconstructs recurrent sequence, slot, gap, position, and morphology-context evidence without importing inherited Kurdish grammar as proof.","",
        "## 1. Full-coverage audit","",
        "| Named source | Expected occurrences | Scanned | Candidate stream | Documentary-only | Containers | Ordering anomalies |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for a in audits:
        lines.append(f"| {a['source']} | {a['expected_occurrences']:,} | {a['scanned_occurrences']:,} | {a['candidate_occurrences']:,} | {a['documentary_only_occurrences']:,} | {a['containers']:,} | {a['ordering_anomalies']:,} |")
    total=sum(a["scanned_occurrences"] for a in audits); cand=sum(a["candidate_occurrences"] for a in audits)
    lines += ["",f"**Verified rows scanned:** **{total:,}**.  **Active structural-candidate occurrences:** **{cand:,}**.","",
              "The difference is preserved documentary material excluded from active structural scoring by the mechanical V2 candidate filter; it is not deleted from the dictionaries.","",
              "## 2. Recurrent continuous and discontinuous structures","",
              "| Candidate type | Cross-source retained patterns |",
              "|---|---:|"]
    for kind in KINDS: lines.append(f"| {kind} | {pattern_results[kind]['cross_source_rows']:,} |")
    for kind in KINDS:
        lines += ["",f"### Highest evidence {kind}","", "| Pattern | Sources | Support | CCES |", "|---|---:|---:|---:|"]
        for r in pattern_results[kind]["top"][:25]:
            if kind=="BIGRAMS": pat=f"`{r['form_1']} {r['form_2']}`"
            elif kind=="TRIGRAMS": pat=f"`{r['form_1']} {r['form_2']} {r['form_3']}`"
            elif kind=="FOURGRAMS": pat=f"`{r['form_1']} {r['form_2']} {r['form_3']} {r['form_4']}`"
            elif kind=="SLOT_FRAMES": pat=f"`{r['left_form']} + SLOT + {r['right_form']}`"
            elif kind=="GAP2": pat=f"`{r['form_1']} _ _ {r['form_2']}`"
            else: pat=f"`{r['form_1']} _ _ _ {r['form_2']}`"
            lines.append(f"| {pat} | {r['source_count']} | {r['aggregate_support']:,} | {r['construction_evidence_score']} |")
    lines += ["","## 3. Morphology-context re-test","",f"V2 re-tested the highest-ranked V1 form-family candidates against complete occurrence contexts. Cross-source candidates surviving the current two-source aggregation threshold: **{len(morph_rows):,}**.","",
              "| Base | Extended | Edge | Material | Sources | Support | Full-context similarity | MCES2 |", "|---|---|---|---|---:|---:|---:|---:|"]
    for r in morph_rows[:40]: lines.append(f"| `{r['base_form']}` | `{r['extended_form']}` | {r['edge_side']} | `{r['added_edge_material']}` | {r['source_count']} | {r['aggregate_min_frequency_support']:,} | {r['mean_full_context_similarity']} | {r['morphology_context_evidence_score_v2']} |")
    lines += ["","## 4. Position system","",f"Cross-source full-occurrence position profiles: **{len(pos_rows):,}** exact forms. Each retains initial/final counts plus ten within-container position bins.","",
              "## 5. Language Graph V2","",f"Graph V2 high-evidence core nodes: **{graph_counts[0]:,}**. Edges: **{graph_counts[1]:,}**.","",
              "Graph nodes include named sources, exact forms, recurrent sequence/frame candidates, and V2-tested form-family candidates. Graph communities remain evidence clusters, not grammatical categories.","",
              "## 6. What V2 establishes","",
              "- complete occurrence-row coverage for every committed corpus;",
              "- exact recurrent continuous sequences under declared thresholds;",
              "- exact variable-slot and discontinuous pattern candidates;",
              "- full candidate-stream position profiles;",
              "- complete immediate-context tests for the selected V1 morphology candidates;",
              "- cross-source recurrence, support, and source-distribution evidence;",
              "- a richer provenance-preserving language graph.","",
              "## 7. What V2 does not establish automatically","",
              "- definitive morphemes, prefixes, or suffixes;",
              "- noun/verb/adjective classes;",
              "- subject/object relations;",
              "- tense/aspect/mood or case systems;",
              "- semantic equivalence of identical spellings;",
              "- pronunciation/phonology from text alone;",
              "- that every letter-bearing candidate belongs to Kurdish.","",
              "# Deep conclusion","",
              "V2 moves the project from a lexicon-neighbor skeleton to a **full-occurrence constructional evidence system**. Recurrent relationships can now be tested as exact sequences, variable-slot frames, discontinuous endpoint patterns, positional profiles, and complete-context form-family relations across independently preserved named sources.","",
              "The next interpretive step is no longer to guess a traditional grammar. It is to take the highest-evidence V2 constructions and form families, inspect their source-local support and counterexamples, compare competing structural explanations, and only then consider conventional linguistic terminology where it demonstrably compresses and predicts the evidence better than alternatives.",""]
    (out/"TSLK_SCIENCES_OF_LANGUAGE_REPORT_V2.md").write_text("\n".join(lines),encoding="utf-8")


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--artifacts-root",required=True); ap.add_argument("--output-root",default="Sciences_of_Language_V2"); args=ap.parse_args()
    artifacts=Path(args.artifacts_root).resolve(); out=Path(args.output_root).resolve(); (out/"Data").mkdir(parents=True,exist_ok=True)
    audits=read_audits(artifacts)
    if len(audits)!=14: raise SystemExit("Need 14 V2 audits")
    total=sum(a["scanned_occurrences"] for a in audits)
    expected=sum(a["expected_occurrences"] for a in audits)
    if total!=expected: raise SystemExit(f"Aggregate coverage mismatch: {total} != {expected}")
    # Source audit table
    audit_rows=[]
    for a in audits:
        audit_rows.append({k:a.get(k,"") for k in ["source","corpus","domain","expected_occurrences","scanned_occurrences","candidate_occurrences","documentary_only_occurrences","containers","active_runs","ordering_anomalies","coverage_pass","ordering_pass"]})
    write_tsv(out/"Data"/"SOURCE_FULL_OCCURRENCE_AUDIT.tsv",list(audit_rows[0]),audit_rows)

    pattern_results={}
    for kind in KINDS: pattern_results[kind]=aggregate_kind(artifacts,out,kind)
    morph_rows=aggregate_morphology(artifacts,out)
    pos_rows=aggregate_positions(artifacts,out)
    graph_counts=graph_v2(out,pattern_results,morph_rows)
    copy_compact_per_source(artifacts,out,pattern_results)
    report(out,audits,pattern_results,morph_rows,pos_rows,graph_counts)

    manifest={
        "version":"TSLK_SCIENCES_OF_LANGUAGE_V2",
        "source_count":14,
        "expected_occurrences":expected,
        "scanned_occurrences":total,
        "full_occurrence_coverage_pass":total==expected,
        "candidate_occurrences":sum(a["candidate_occurrences"] for a in audits),
        "documentary_only_occurrences":sum(a["documentary_only_occurrences"] for a in audits),
        "cross_source_pattern_counts":{k:v["cross_source_rows"] for k,v in pattern_results.items()},
        "morphology_context_candidates_cross_source":len(morph_rows),
        "cross_source_position_profiles":len(pos_rows),
        "language_graph_v2_nodes":graph_counts[0],
        "language_graph_v2_edges":graph_counts[1],
        "scores_are_truth_probabilities":False,
        "semantic_assignment_performed":False,
        "conventional_grammar_assignment_performed":False,
        "native_speaker_stream_used":False,
        "candidate_stream_is_language_membership_classifier":False,
        "per_source_full_pattern_tables_storage":"GitHub Actions build artifacts; deterministic from repository-resident occurrence shards. Repository contains top-5000 per source plus complete cross-source promoted tables.",
    }
    (out/"SCIENCES_OF_LANGUAGE_V2_MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    audit_text=["# TSLK Sciences of Language V2 — Build Audit","", "**PASS**" if total==expected else "**FAIL**","",f"- Expected occurrence rows: **{expected:,}**",f"- Scanned occurrence rows: **{total:,}**",f"- 14/14 corpus coverage manifests present: **YES**",f"- Conventional grammar assignment: **NO**",f"- Semantic assignment: **NO**",f"- Native-speaker Stream B used: **NO**","", "V2 candidate filtering is mechanical and does not prove Kurdish language membership. Cross-source tables contain only patterns attested in at least two named sources after per-source recurrence thresholds."]
    (out/"TSLK_SCIENCES_OF_LANGUAGE_AUDIT_V2.md").write_text("\n".join(audit_text)+"\n",encoding="utf-8")

if __name__=="__main__": main()
