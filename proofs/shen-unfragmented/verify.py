from itertools import combinations, permutations
from math import factorial, prod
from random import Random

def edges(vertices):
    return tuple(combinations(sorted(vertices), 2))

def fragmented(vertices, order):
    remaining = set(vertices)
    while len(remaining) >= 2:
        induced = [e for e in order if set(e) <= remaining]
        prefix = induced[:len(remaining)-1]
        centers = set.intersection(*(set(e) for e in prefix))
        if not centers:
            return False
        remaining.remove(min(centers))
    return True

def local(vertices, order):
    return all(fragmented(s, order) for s in combinations(vertices, 4))

def generated(vertices):
    if len(vertices) <= 2:
        yield edges(vertices)
        return
    for v in vertices:
        rest = tuple(w for w in vertices if w != v)
        star = tuple(tuple(sorted((v,w))) for w in rest)
        for tail in generated(rest):
            for head in permutations(star):
                yield head + tail

def count(n):
    return factorial(n)//2 * prod(factorial(j) for j in range(1,n))

def main():
    v = tuple(range(4))
    n_good = 0
    for order in permutations(edges(v)):
        actual = fragmented(v,order)
        expected = len(set.intersection(*(set(e) for e in order[:3]))) == 1
        assert actual == expected
        assert actual == local(v,order)
        n_good += actual
    assert n_good == count(4)
    print(f'n=4: all 720 orders checked, {n_good} fragmented: PASS')
    v = tuple(range(5))
    all_good = set(generated(v))
    assert len(all_good) == count(5) == 17280
    assert all(fragmented(v,o) and local(v,o) for o in all_good)
    print('n=5: all 17,280 generated fragmented orders verified: PASS')
    rng = Random(488756)
    for n in (5,6,7):
        v = tuple(range(n)); order = list(edges(v))
        for _ in range(5000):
            rng.shuffle(order)
            assert fragmented(v,order) == local(v,order)
        print(f'n={n}: 5,000 deterministic sampled orders: PASS')

if __name__ == '__main__':
    main()
