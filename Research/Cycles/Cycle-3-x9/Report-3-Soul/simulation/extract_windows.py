"""Coder C input for SIM-R3-C3 (run once; needs the source snapshots, which are not in the repository). Extract fixed text windows around each conception's key terms from the cited source snapshots (input for coder C, SIM-R3-C3).
Key terms were written before any coding; windows are 1200 characters centred on each match (max 8 per conception and source)."""
import csv, json, re, hashlib
SNAP = "/workspace/gaia/snap_all/"; OUT = "/workspace/gaia/c3/Research/Cycles/Cycle-3-x9/Report-3-Soul/simulation/data/window_hits_c3.json"
KEY = {"C01": r"Plato|Phaedo", "C02": r"Aristotle|De Anima", "C03": r"Epicur", "C04": r"Stoic|pneuma", "C05": r"nephesh|nefesh|living being|Genesis 2",
       "C06": r"Aquinas", "C07": r"\bru[hḥ]\b|rūḥ|spirit", "C08": r"\bsoul\b|[aā]tman", "C09": r"Advaita|[aā]tman|Brahman", "C10": r"an[aā]tman|no-self|not-self",
       "C11": r"\bhun\b|\bpo\b|\bqi\b|\bxin\b", "C12": r"Akan|Gyekye|okra", "C13": r"animis|relational", "C14": r"physicalis", "C15": r"j[iī]va"}
LEX = {  # coder C lexicon, written before coding (case-insensitive, word-start anchored)
 "A1_immaterial": r"incorporeal|immaterial|non-?physical|not a body|not material|spiritual substance|not made of matter",
 "A2_independent_of_body_survives_death": r"immortal|surviv|after death|afterlife|rebirth|reincarnat|transmigrat|resurrect|not killed|never dies|eternal life",
 "A3_principle_of_life_or_breath": r"breath|life-giving|principle of life|animat|alive|living being|pneuma|vital",
 "A4_seat_of_thought_or_identity": r"think|intellect|reason|knower|mind\b|conscious|true self|identity",
 "A5_bearer_of_moral_character": r"virtue|vice|karma|moral|evil|sin\b|righteous|merit|character",
 "A6_oriented_to_purpose_or_final_end": r"liberation|mok[sṣ]a|nirvana|salvation|telos|final end|goal|purpose|happiness",
 "A7_enduring_unchanging_self": r"eternal|unchanging|permanent|immutable|everlasting|imperishable|unborn",
 "A8_form_of_or_inseparable_from_body": r"form of the body|form of a|organi[sz]ation|inseparable|cannot exist apart|function of the body|perishes with|dies with",
 "A9_enduring_self_denied": r"no-self|not-self|an[aā]tman|no soul|no enduring self|without self",
 "A10_constituted_relationally_or_communally": r"relational|communit|communal|social|personhood|kin\b|kinship|relationship",
 "A11_identical_with_universal_ground": r"brahman|universal|ultimate reality|one with",
 "A12_extends_to_non_human_beings": r"animal|plant|non-?human|all living|tree|rivers|mountain"}
SIZES = [300, 600, 1200]
rows = list(csv.DictReader(open("/workspace/gaia/c3/Research/Cycles/Cycle-2-x6/Report-3-Soul/simulation/data/coding_c1.csv")))
out = dict(note=__doc__, sizes=SIZES, max_windows=8, key_terms=KEY, lexicon=None, conceptions={})
for r in rows:
    W = []; srcs = {}
    for s in r["source"].split(";"):
        t = open(SNAP + s + ".txt", errors="ignore").read(); srcs[s] = hashlib.sha256(t.encode()).hexdigest()
        t = re.sub(r"\s+", " ", t)
        for m in list(re.finditer(KEY[r["id"]], t, re.I))[:8]:
            c = (m.start()+m.end())//2; W.append(dict(source=s, offset=m.start(), hits={str(z): sorted(a for a, rx in LEX.items() if re.search(r"\b(?:" + rx + ")", t[max(0, c-z//2):c+z//2], re.I)) for z in SIZES}))
    out["conceptions"][r["id"]] = dict(conception=r["conception"], sources=srcs, windows=W)
    print(r["id"], len(W))
out["lexicon"] = LEX
json.dump(out, open(OUT, "w", newline="\n"), indent=1, ensure_ascii=False); open(OUT, "a").write("\n")
