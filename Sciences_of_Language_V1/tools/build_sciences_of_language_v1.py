#!/usr/bin/env python3
from __future__ import annotations

import csv, gzip, json, math, re, unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]
DROOT = ROOT / "Dictionaries"
CROOT = ROOT / "Comparative_Research_V1"
OUT = ROOT / "Sciences_of_Language_V1"
DATA = OUT / "Data"
GRAPH = OUT / "Graph"
DATA.mkdir(parents=True, exist_ok=True)
GRAPH.mkdir(parents=True, exist_ok=True)

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


def is_letter_candidate(s: str) -> bool:
    cats = [unicodedata.category(ch) for ch in s]
    return any(c.startswith("L") for c in cats) and not any(c.startswith("N") for c in cats)


def parse_neighbors(s: str):
    out=[]
    if not s: return out
    for part in s.split(" | "):
        if "::" not in part: continue
        form, count = part.rsplit("::",1)
        try: n=int(count)
        except ValueError: continue
        if form: out.append((form,n))
    return out


def entropy_norm(counter: Counter) -> float:
    vals=[v for v in counter.values() if v>0]
    if len(vals)<=1: return 0.0
    total=sum(vals); h=0.0
    for v in vals:
        p=v/total; h -= p*math.log(p)
    return h/math.log(len(vals))


def jaccard(a:set,b:set)->float:
    u=a|b
    return len(a&b)/len(u) if u else 0.0


def write_tsv(path, fields, rows, gz=False):
    opener = gzip.open if gz else open
    kwargs = {"encoding":"utf-8","newline":""}
    if gz: kwargs["mode"]="wt"
    else: kwargs["mode"]="w"
    with opener(path, **kwargs) as f:
        w=csv.DictWriter(f, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        w.writeheader(); w.writerows(rows)


def load_template_risk():
    risk=set()
    p=CROOT/"Data"/"LETTER_BEARING_CROSS_SOURCE_INDEX.tsv.gz"
    if not p.exists(): return risk
    with gzip.open(p,"rt",encoding="utf-8",newline="") as f:
        for r in csv.DictReader(f,delimiter="\t"):
            if r.get("repeated_context_template_risk")=="YES": risk.add(r.get("surface_form",""))
    return risk


def load_sources():
    all_entries={}
    for folder,_,_ in SOURCES:
        entries={}
        files=sorted((DROOT/folder).glob("LEXICON_*.tsv"))
        if not files and (DROOT/folder/"LEXICON.tsv").exists(): files=[DROOT/folder/"LEXICON.tsv"]
        for p in files:
            with p.open("r",encoding="utf-8",newline="") as f:
                for r in csv.DictReader(f,delimiter="\t"):
                    form=r.get("surface_form","")
                    if not form or not is_letter_candidate(form): continue
                    def iv(k):
                        try:return int(r.get(k,"0") or 0)
                        except:return 0
                    neigh=set(x for x,_ in parse_neighbors(r.get("top_left_neighbors","")+" | "+r.get("top_right_neighbors","")) if is_letter_candidate(x))
                    entries[form]={
                        "frequency":iv("frequency"),
                        "initial":iv("container_initial_count"),
                        "final":iv("container_final_count"),
                        "left":parse_neighbors(r.get("top_left_neighbors","")),
                        "right":parse_neighbors(r.get("top_right_neighbors","")),
                        "neighbors":neigh,
                        "first_context":r.get("first_context","") or "",
                        "length":len(form),
                    }
        all_entries[folder]=entries
    return all_entries


def score_support(source_counts:Counter, total_support:int, max_support:int, source_weight=.45, support_weight=.35, entropy_weight=.20):
    sd=len(source_counts)/N_SOURCES
    sn=math.log1p(total_support)/math.log1p(max_support) if max_support>0 else 0
    en=entropy_norm(source_counts)
    return 100*(source_weight*sd+support_weight*sn+entropy_weight*en)


def main():
    risk=load_template_risk()
    entries=load_sources()
    membership=defaultdict(list); global_freq=Counter()
    for folder,_,_ in SOURCES:
        for form,m in entries[folder].items():
            membership[form].append(folder); global_freq[form]+=m["frequency"]

    # Source science/literature profiles
    source_rows=[]; literature_rows=[]
    for folder,name,domain in SOURCES:
        e=entries[folder]; types=len(e); toks=sum(x["frequency"] for x in e.values())
        hapax=sum(1 for x in e.values() if x["frequency"]==1)
        shared=sum(1 for form in e if len(membership[form])>=2)
        riskn=sum(1 for form in e if form in risk)
        avglen=sum(len(form)*m["frequency"] for form,m in e.items())/toks if toks else 0
        init=sum(m["initial"] for m in e.values()); fin=sum(m["final"] for m in e.values())
        row={
            "source":name,"folder":folder,"domain":domain,"letter_bearing_types":types,"letter_bearing_occurrences":toks,
            "type_token_ratio":f"{types/toks if toks else 0:.8f}","hapax_types":hapax,"hapax_type_share":f"{hapax/types if types else 0:.8f}",
            "shared_2plus_types":shared,"shared_2plus_share":f"{shared/types if types else 0:.8f}","template_risk_types":riskn,
            "weighted_mean_graphemic_length":f"{avglen:.4f}","container_initial_occurrences":init,"container_final_occurrences":fin,
        }
        source_rows.append(row); literature_rows.append(row.copy())
    write_tsv(DATA/"SOURCE_LANGUAGE_SCIENCE_PROFILE.tsv", list(source_rows[0]), source_rows)
    write_tsv(DATA/"LITERATURE_REGISTER_PROFILE.tsv", list(literature_rows[0]), literature_rows)

    # Form structure profile for shared non-risk candidates
    form_rows=[]
    for form,srcs in membership.items():
        if len(srcs)<2 or form in risk: continue
        freq=global_freq[form]
        init=sum(entries[s][form]["initial"] for s in srcs); fin=sum(entries[s][form]["final"] for s in srcs)
        total=sum(entries[s][form]["frequency"] for s in srcs)
        form_rows.append({"surface_form":form,"source_count":len(srcs),"sources":" | ".join(DISPLAY[s] for s in srcs),
                          "aggregate_frequency":freq,"graphemic_length":len(form),"aggregate_initial_count":init,"aggregate_final_count":fin,
                          "initial_rate":f"{init/total if total else 0:.8f}","final_rate":f"{fin/total if total else 0:.8f}",
                          "template_risk":"NO","semantic_status":"UNRESOLVED","grammatical_status":"UNRESOLVED"})
    form_rows.sort(key=lambda r:(-r["source_count"],-r["aggregate_frequency"],r["surface_form"].casefold(),r["surface_form"]))
    write_tsv(DATA/"FORM_STRUCTURE_PROFILE.tsv.gz", list(form_rows[0]), form_rows, gz=True)

    # Edge-extension / morphology candidates
    rel=defaultdict(lambda:{"sources":set(),"support":Counter(),"context":[]})
    pattern=defaultdict(lambda:{"sources":set(),"pairs":set(),"support":0,"context":[]})
    for folder,_,_ in SOURCES:
        e=entries[folder]; forms=set(e)
        for ext,m in e.items():
            if ext in risk or len(ext)<2: continue
            for k in (1,2,3):
                if len(ext)<=k: continue
                for side,base,added in (("LEFT",ext[k:],ext[:k]),("RIGHT",ext[:-k],ext[-k:])):
                    if base not in forms or base in risk or not is_letter_candidate(base): continue
                    key=(base,ext,side,added)
                    support=min(e[base]["frequency"],m["frequency"])
                    cs=jaccard(e[base]["neighbors"],m["neighbors"])
                    rel[key]["sources"].add(folder); rel[key]["support"][folder]+=support; rel[key]["context"].append(cs)
                    pk=(side,added); pattern[pk]["sources"].add(folder); pattern[pk]["pairs"].add((base,ext)); pattern[pk]["support"]+=support; pattern[pk]["context"].append(cs)
    max_rel=max((sum(v["support"].values()) for v in rel.values()),default=1)
    rel_rows=[]
    for (base,ext,side,added),v in rel.items():
        sc=len(v["sources"]); supp=sum(v["support"].values()); ctx=sum(v["context"])/len(v["context"]) if v["context"] else 0
        sd=sc/N_SOURCES; sn=math.log1p(supp)/math.log1p(max_rel); score=100*(.40*sd+.30*sn+.30*ctx)
        rel_rows.append({"base_form":base,"extended_form":ext,"edge_side":side,"added_edge_material":added,"source_count":sc,
                         "sources":" | ".join(DISPLAY[s] for s in sorted(v["sources"])),"aggregate_min_frequency_support":supp,
                         "mean_neighbor_context_jaccard":f"{ctx:.8f}","form_family_evidence_score":f"{score:.4f}",
                         "interpretation_status":"EDGE-EXTENSION CANDIDATE / FUNCTION UNRESOLVED"})
    rel_rows.sort(key=lambda r:(-float(r["form_family_evidence_score"]),-r["source_count"],-r["aggregate_min_frequency_support"]))
    write_tsv(DATA/"FORM_FAMILY_CANDIDATES.tsv.gz", list(rel_rows[0]), rel_rows, gz=True)

    max_pat=max((v["support"] for v in pattern.values()),default=1)
    pat_rows=[]
    for (side,added),v in pattern.items():
        ctx=sum(v["context"])/len(v["context"]) if v["context"] else 0
        score=100*(.40*len(v["sources"])/N_SOURCES+.30*math.log1p(v["support"])/math.log1p(max_pat)+.30*ctx)
        pat_rows.append({"edge_side":side,"edge_material":added,"source_count":len(v["sources"]),"supporting_distinct_form_pairs":len(v["pairs"]),
                         "aggregate_min_frequency_support":v["support"],"mean_neighbor_context_jaccard":f"{ctx:.8f}",
                         "edge_material_evidence_score":f"{score:.4f}","status":"RECURRING EDGE-MATERIAL PATTERN / FUNCTION UNRESOLVED"})
    pat_rows.sort(key=lambda r:(-float(r["edge_material_evidence_score"]),-r["source_count"],-r["supporting_distinct_form_pairs"]))
    write_tsv(DATA/"EDGE_MATERIAL_PATTERNS.tsv", list(pat_rows[0]), pat_rows)

    # Structural neighbor candidates
    edges=defaultdict(Counter)
    for folder,_,_ in SOURCES:
        e=entries[folder]
        for a,m in e.items():
            if a in risk: continue
            for b,n in m["right"]:
                if not is_letter_candidate(b) or b in risk: continue
                edges[(a,b)][folder]+=n
    kept={k:v for k,v in edges.items() if len(v)>=2 and sum(v.values())>=5}
    max_edge=max((sum(v.values()) for v in kept.values()),default=1)
    edge_rows=[]
    for (a,b),v in kept.items():
        total=sum(v.values()); score=score_support(v,total,max_edge)
        edge_rows.append({"left_form":a,"right_form":b,"source_count":len(v),"sources":" | ".join(DISPLAY[s] for s in sorted(v)),
                          "aggregate_top_neighbor_support":total,"source_entropy":f"{entropy_norm(v):.8f}","structural_evidence_score":f"{score:.4f}",
                          "status":"STRUCTURAL NEIGHBOR CANDIDATE / RELATION UNRESOLVED"})
    edge_rows.sort(key=lambda r:(-float(r["structural_evidence_score"]),-r["source_count"],-r["aggregate_top_neighbor_support"]))
    write_tsv(DATA/"STRUCTURAL_NEIGHBOR_CANDIDATES.tsv.gz", list(edge_rows[0]), edge_rows, gz=True)

    # Positional candidates
    pos_rows=[]
    for form,srcs in membership.items():
        if len(srcs)<2 or form in risk: continue
        freq=sum(entries[s][form]["frequency"] for s in srcs); init=sum(entries[s][form]["initial"] for s in srcs); fin=sum(entries[s][form]["final"] for s in srcs)
        ir=init/freq if freq else 0; fr=fin/freq if freq else 0; strength=max(ir,fr)
        score=100*(.5*len(srcs)/N_SOURCES+.5*strength)
        pos_rows.append({"surface_form":form,"source_count":len(srcs),"aggregate_frequency":freq,"initial_count":init,"final_count":fin,
                         "initial_rate":f"{ir:.8f}","final_rate":f"{fr:.8f}","dominant_observed_position":"INITIAL" if ir>fr else "FINAL" if fr>ir else "BALANCED",
                         "positional_evidence_score":f"{score:.4f}","status":"POSITIONAL TENDENCY / FUNCTION UNRESOLVED"})
    pos_rows.sort(key=lambda r:(-float(r["positional_evidence_score"]),-r["source_count"],-r["aggregate_frequency"]))
    write_tsv(DATA/"POSITIONAL_CANDIDATES.tsv.gz", list(pos_rows[0]), pos_rows, gz=True)

    # Language graph
    node_forms=set(r["surface_form"] for r in form_rows)
    node_rows=[]
    for folder,name,_ in SOURCES: node_rows.append({"node_id":"SRC:"+folder,"node_type":"SOURCE","label":name,"source_count":"","aggregate_frequency":"","status":"SOURCE"})
    for r in form_rows:
        node_rows.append({"node_id":"FORM:"+r["surface_form"],"node_type":"FORM","label":r["surface_form"],"source_count":r["source_count"],"aggregate_frequency":r["aggregate_frequency"],"status":"LANGUAGE MEMBERSHIP UNRESOLVED"})
    for i,r in enumerate(pat_rows[:500],1): node_rows.append({"node_id":f"PAT:{i:04d}","node_type":"EDGE_MATERIAL_PATTERN","label":r["edge_side"]+":"+r["edge_material"],"source_count":r["source_count"],"aggregate_frequency":r["aggregate_min_frequency_support"],"status":"FUNCTION UNRESOLVED"})
    write_tsv(GRAPH/"LANGUAGE_GRAPH_NODES.tsv.gz", ["node_id","node_type","label","source_count","aggregate_frequency","status"], node_rows, gz=True)

    graph_edges=[]
    for form,srcs in membership.items():
        if form not in node_forms: continue
        for s in srcs: graph_edges.append({"from":"SRC:"+s,"to":"FORM:"+form,"edge_type":"SOURCE_ATTESTS_FORM","evidence_score":"","support":"1"})
    for r in edge_rows:
        if r["left_form"] in node_forms and r["right_form"] in node_forms:
            graph_edges.append({"from":"FORM:"+r["left_form"],"to":"FORM:"+r["right_form"],"edge_type":"FORM_NEIGHBOR_FORM","evidence_score":r["structural_evidence_score"],"support":r["aggregate_top_neighbor_support"]})
    for r in rel_rows:
        if r["base_form"] in node_forms and r["extended_form"] in node_forms and r["source_count"]>=2:
            graph_edges.append({"from":"FORM:"+r["base_form"],"to":"FORM:"+r["extended_form"],"edge_type":"FORM_EDGE_EXTENSION_FORM","evidence_score":r["form_family_evidence_score"],"support":r["aggregate_min_frequency_support"]})
    write_tsv(GRAPH/"LANGUAGE_GRAPH_EDGES.tsv.gz", ["from","to","edge_type","evidence_score","support"], graph_edges, gz=True)

    # Compact GraphML core: top forms + top structural/morph edges
    top_forms=set(r["surface_form"] for r in form_rows[:25000])
    core_edges=[]
    for r in edge_rows[:20000]:
        if r["left_form"] in top_forms and r["right_form"] in top_forms: core_edges.append(("FORM:"+r["left_form"],"FORM:"+r["right_form"],"NEIGHBOR",r["structural_evidence_score"]))
    for r in rel_rows[:20000]:
        if r["base_form"] in top_forms and r["extended_form"] in top_forms and r["source_count"]>=2: core_edges.append(("FORM:"+r["base_form"],"FORM:"+r["extended_form"],"EDGE_EXTENSION",r["form_family_evidence_score"]))
    with gzip.open(GRAPH/"LANGUAGE_GRAPH_CORE.graphml.gz","wt",encoding="utf-8") as g:
        g.write('<?xml version="1.0" encoding="UTF-8"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns">\n<graph edgedefault="directed">\n')
        for folder,name,_ in SOURCES: g.write(f'<node id="{escape("SRC:"+folder)}"><data key="label">{escape(name)}</data></node>\n')
        for form in sorted(top_forms): g.write(f'<node id="{escape("FORM:"+form)}"><data key="label">{escape(form)}</data></node>\n')
        eid=0
        for form in top_forms:
            for s in membership[form]: eid+=1; g.write(f'<edge id="e{eid}" source="{escape("SRC:"+s)}" target="{escape("FORM:"+form)}"><data key="type">ATTESTS</data></edge>\n')
        for a,b,t,sc in core_edges: eid+=1; g.write(f'<edge id="e{eid}" source="{escape(a)}" target="{escape(b)}"><data key="type">{t}</data><data key="score">{sc}</data></edge>\n')
        g.write('</graph>\n</graphml>\n')

    # Integrated report
    report=[]
    report += ["# Kurdish-TSL — The Sciences of Language Structural Report V1","",
               "## Scientific status","",
               "This report builds a structural evidence model from the fourteen named corpora, Deep Dictionary V1, and Comparative Research V1. It does **not** import inherited Kurdish grammar as proof. Morphology and grammar labels below are candidate domains, not pre-decided categories.",""]
    report += ["## 1. Source and literature/register landscape","",
               "| Named source | Domain | Letter-bearing types | Occurrences | Hapax share | Shared ≥2 share | Mean graphemic length |","|---|---|---:|---:|---:|---:|---:|"]
    for r in source_rows:
        report.append(f"| {r['source']} | {r['domain']} | {r['letter_bearing_types']:,} | {r['letter_bearing_occurrences']:,} | {100*float(r['hapax_type_share']):.2f}% | {100*float(r['shared_2plus_share']):.2f}% | {r['weighted_mean_graphemic_length']} |")
    report += ["","## 2. Word-structure system","",f"- Shared, non-template-risk letter-bearing form profiles: **{len(form_rows):,}**.",
               "- Each profile preserves source count, aggregate frequency, graphemic length, and positional evidence.",""]
    report += ["## 3. Morphology-candidate system","",f"- Exact edge-extension form-family candidates: **{len(rel_rows):,}**.",f"- Recurrent edge-material patterns: **{len(pat_rows):,}**.",
               "- These do not yet prove morphemes. They identify written relations worth direct contextual testing.",""]
    report += ["### Highest evidence edge-material patterns","","| Side | Material | Sources | Distinct pairs | Support | Score |","|---|---|---:|---:|---:|---:|"]
    for r in pat_rows[:30]: report.append(f"| {r['edge_side']} | `{r['edge_material']}` | {r['source_count']} | {r['supporting_distinct_form_pairs']:,} | {r['aggregate_min_frequency_support']:,} | {r['edge_material_evidence_score']} |")
    report += ["","## 4. Structural / grammar-candidate system","",f"- Cross-source immediate-neighbor candidates meeting V1 thresholds: **{len(edge_rows):,}**.",
               "- The Structural Evidence Score rewards source diversity, support, and source-distribution entropy; it is not a grammar-correctness probability.",""]
    report += ["### Highest structural evidence relations","","| Left form | Right form | Sources | Support | SES |","|---|---|---:|---:|---:|"]
    for r in edge_rows[:40]: report.append(f"| `{r['left_form']}` | `{r['right_form']}` | {r['source_count']} | {r['aggregate_top_neighbor_support']:,} | {r['structural_evidence_score']} |")
    report += ["","## 5. Positional system","",f"- Cross-source positional candidates: **{len(pos_rows):,}**.",
               "- Initial/final tendencies remain descriptive until direct constructional analysis explains them.",""]
    report += ["## 6. Language graph","",f"- Graph nodes: **{len(node_rows):,}**.",f"- Graph edges: **{len(graph_edges):,}**.",
               "- Node types: SOURCE, FORM, EDGE_MATERIAL_PATTERN.","- Edge types: SOURCE_ATTESTS_FORM, FORM_NEIGHBOR_FORM, FORM_EDGE_EXTENSION_FORM.",
               "- A compact GraphML core is included for graph software; exhaustive graph tables remain in gzipped TSV.",""]
    report += ["## 7. What is mechanically established","",
               "- exact written-form recurrence and source incidence;","- local neighbor recurrence from the dictionary profiles;","- container-edge positional counts;","- graphemic edge-extension relations;","- source/register quantitative differences;","- graph topology of these evidence relations.",""]
    report += ["## 8. What is not yet established","",
               "- definitive morphemes or affixes;","- noun/verb/adjective classes;","- subject/object relations;","- tense/aspect/mood categories;","- case/ergativity systems;","- pronunciation or phonology from text alone;","- semantic identity of same-spelled forms across sources;","- complete grammar over the 47.6M occurrence stream.",""]
    report += ["# Deep conclusion","",
               "The evidence now supports a real **structural language graph** rather than a flat dictionary. Written forms are connected simultaneously by source membership, local adjacency, positional behavior, and graphemic edge-extension relations. This creates a testable architecture in which candidate word families and candidate constructions can be ranked before interpretation.","",
               "The strongest methodological gain is that morphology and grammar can now be approached as graph problems: a proposed unit must explain multiple form relations, recur in independently preserved sources, survive source imbalance, and fit observed contexts better than competing analyses. A familiar grammatical label is therefore an output of future testing, not an input to this graph.","",
               "The literature/register layer also shows why one unified frequency list is insufficient: each named source has a different scale, one-occurrence-form profile, overlap rate, and positional/neighbor structure. A future grammar must explain both the recurrent cross-source core and the source-specific variation instead of normalizing the latter away.","",
               "V1 therefore establishes the computational skeleton for the Sciences of Language project. The next upgrade is V2: scan the full 47.6M occurrence stream for unrestricted n-gram, discontinuous, positional, and construction-network evidence, then test the highest V1 morphology/structural candidates against their complete source-local contexts."]
    (OUT/"TSLK_SCIENCES_OF_LANGUAGE_REPORT_V1.md").write_text("\n".join(report)+"\n",encoding="utf-8")

    manifest={
        "version":"TSLK_SCIENCES_OF_LANGUAGE_V1",
        "source_count":N_SOURCES,
        "shared_non_template_form_profiles":len(form_rows),
        "form_family_edge_extension_candidates":len(rel_rows),
        "edge_material_patterns":len(pat_rows),
        "structural_neighbor_candidates":len(edge_rows),
        "positional_candidates":len(pos_rows),
        "language_graph_nodes":len(node_rows),
        "language_graph_edges":len(graph_edges),
        "scores_are_truth_probabilities":False,
        "semantic_assignment_performed":False,
        "conventional_grammar_assignment_performed":False,
        "stage4_failed_claims_used_as_proof":False,
        "full_47m_occurrence_sequence_grammar_performed":False,
        "scope_note":"V1 uses lexicon-level top-neighbor and position profiles; unrestricted occurrence-sequence grammar is reserved for V2.",
    }
    (OUT/"SCIENCES_OF_LANGUAGE_MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(manifest,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
