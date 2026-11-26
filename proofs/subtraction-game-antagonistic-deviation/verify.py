from functools import cache

S = (5, 7, 18, 23, 24)

@cache
def outcome(h, a, b):
    candidates = []
    for s in S:
        if s <= h:
            y, x = outcome(h-s, b, a)
            candidates.append((s+x, y))
    if not candidates:
        return (0, 0)
    best = max(x for x, y in candidates)
    tie = max if a == "F" else min
    return best, tie(y for x, y in candidates if x == best)

expected = {("A", "A"): (79, 74), ("A", "F"): (79, 73),
            ("F", "A"): (79, 74), ("F", "F"): (79, 74)}
for (a, b), value in expected.items():
    assert outcome(153, a, b) == value
    print(a+b, value)
assert outcome(153, "A", "A")[1] > outcome(153, "A", "F")[1]
