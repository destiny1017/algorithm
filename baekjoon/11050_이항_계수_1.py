# https://www.acmicpc.net/problem/11050
from itertools import *

# p = list(permutations(["A","B","C"], 2))
# l = list(combinations(["A", "B", "C"], 2))
# list1 = list(combinations([1] * 5, 2))
# print(p)
# print(l)
# print(len(list1))
n, k = map(int, input().split())
print(len(list(combinations([1] * n, k))))

