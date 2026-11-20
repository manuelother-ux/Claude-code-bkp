#!/usr/bin/env python3
"""ISO 2859-1 / ANSI Z1.4 single sampling plan, normal inspection.

Usage:
  python3 aql.py <lot_size> [--level II] [--aql 0,2.5,4.0]
  python3 aql.py --selftest

AQL 0 means zero tolerance (critical defects): sample size of the code letter,
accept 0 / reject 1.

Table II-A is encoded structurally: along each row the cell sequence is
Ac0, up-arrow, down-arrow, 1, 2, 3, 5, 7, 10, 14, 21. Arrows are resolved to
the first plan above / below, using THAT plan's sample size (as the standard says).
Spot-check edge cases (very small lots, letters P-R) against the official table.
"""
import sys

LOTS = [8, 15, 25, 50, 90, 150, 280, 500, 1200, 3200, 10000, 35000, 150000, 500000, float("inf")]
LEVELS = {
    "S-1": "AAAABBBBCCCCDDD",
    "S-2": "AAABBBCCCDDDDEE",
    "S-3": "AABBCCDDEEFFGGH",
    "S-4": "AABCCDEEFGGHJJK",
    "I":   "AABCCDEFGHJKLMN",
    "II":  "ABCDEFGHJKLMNPQ",
    "III": "BCDEFGHJKLMNPQR",
}
LETTERS = "ABCDEFGHJKLMNPQR"
N = dict(zip(LETTERS, [2, 3, 5, 8, 13, 20, 32, 50, 80, 125, 200, 315, 500, 800, 1250, 2000]))
AQLS = [0.010, 0.015, 0.025, 0.040, 0.065, 0.10, 0.15, 0.25, 0.40, 0.65, 1.0, 1.5, 2.5, 4.0, 6.5, 10.0]
SEQ = {0: 0, 3: 1, 4: 2, 5: 3, 6: 5, 7: 7, 8: 10, 9: 14, 10: 21}


def code_letter(lot, level="II"):
    for i, hi in enumerate(LOTS):
        if lot <= hi:
            return LEVELS[level][i]


def plan(letter, aql):
    """Return (sample_size, Ac, Re, letter_used)."""
    if aql == 0:
        return N[letter], 0, 1, letter
    k = min(range(len(AQLS)), key=lambda j: abs(AQLS[j] - aql))
    if abs(AQLS[k] - aql) > 1e-9:
        raise ValueError(f"AQL {aql} not in table {AQLS}")
    i = LETTERS.index(letter)
    while True:
        d = i + k - 14
        if d in SEQ:
            break
        if d < 0 or d == 2:          # down arrow
            if i + 1 >= len(LETTERS):  # nothing below R -> go up instead
                i -= 1
                continue
            i += 1
        else:                         # d == 1 or d > 10: up arrow
            i -= 1
    ac = SEQ[d]
    L = LETTERS[i]
    return N[L], ac, ac + 1, L


def run(lot, level="II", aqls=(0, 2.5, 4.0)):
    letter = code_letter(lot, level)
    out = {"lot": lot, "level": level, "code_letter": letter, "plans": {}}
    for a in aqls:
        n, ac, re_, L = plan(letter, a)
        if n > lot:
            n, ac, re_ = lot, 0, 1  # sample larger than lot -> 100% inspection
            L = "100%"
        out["plans"][a] = {"sample": n, "accept": ac, "reject": re_, "letter_used": L}
    return out


def selftest():
    # Known values from the published ISO 2859-1 Table I / II-A
    assert code_letter(1000) == "J" and code_letter(3000) == "K" and code_letter(5000) == "L"
    assert plan("K", 2.5)[:3] == (125, 7, 8)
    assert plan("K", 4.0)[:3] == (125, 10, 11)
    assert plan("K", 1.5)[:3] == (125, 5, 6)
    assert plan("K", 0.65)[:3] == (125, 2, 3)
    assert plan("L", 2.5)[:3] == (200, 10, 11)
    assert plan("L", 4.0)[:3] == (200, 14, 15)
    assert plan("J", 2.5)[:3] == (80, 5, 6)
    assert plan("J", 4.0)[:3] == (80, 7, 8)
    assert plan("H", 2.5)[:3] == (50, 3, 4)
    assert plan("H", 4.0)[:3] == (50, 5, 6)
    assert plan("M", 2.5)[:3] == (315, 14, 15)
    assert plan("M", 4.0)[:3] == (315, 21, 22)
    assert plan("G", 2.5)[:3] == (32, 2, 3)
    assert plan("F", 2.5)[:3] == (20, 1, 2)
    assert plan("E", 1.0)[:3] == (13, 0, 1)
    assert plan("D", 2.5)[:3] == (5, 0, 1)     # up arrow -> letter C
    assert plan("N", 2.5)[:3] == (500, 21, 22)
    assert plan("N", 4.0)[:3] == (315, 21, 22)  # up arrow -> letter M
    print("selftest OK")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    if a[0] == "--selftest":
        selftest(); sys.exit(0)
    lot = int(a[0]); level = "II"; aqls = (0, 2.5, 4.0)
    if "--level" in a: level = a[a.index("--level") + 1]
    if "--aql" in a: aqls = tuple(float(x) for x in a[a.index("--aql") + 1].split(","))
    r = run(lot, level, aqls)
    print(f"Lot {r['lot']}  level {r['level']}  code letter {r['code_letter']}")
    for k, p in r["plans"].items():
        label = "critical (0)" if k == 0 else f"AQL {k}"
        print(f"  {label:<13} sample {p['sample']:>5}  accept <= {p['accept']}  reject >= {p['reject']}  (letter {p['letter_used']})")
