# https://www.acmicpc.net/problem/15655
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
results = []
for case in sorted(combinations(items, m)):
    results.append(sorted(case))

results.sort()
for result in results:
    print(" ".join(str(x) for x in result))

