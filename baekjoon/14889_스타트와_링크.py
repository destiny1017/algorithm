# https://www.acmicpc.net/problem/14889
from itertools import combinations, permutations
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
items = [i+1 for i in range(n)]

# 한 팀에 구성할 수 있는 인원의 경우의 수 구하기
cases = list(combinations(items, n // 2))
diff = 2**31

# 경우의 수의 절반 만큼을 순회하며, 첫 팀과 끝 팀의 점수 차 구하기(정렬 조합이므로 가능)
for i in range(len(cases)//2):
    a_case = list(permutations(cases[i], 2))
    b_case = list(permutations(cases[len(cases) - 1 - i], 2))

    point_a = 0
    point_b = 0
    for j in range(len(a_case)):
        point_a += arr[a_case[j][0]-1][a_case[j][1]-1]
        point_b += arr[b_case[j][0]-1][b_case[j][1]-1]

    diff = min(diff, abs(point_a - point_b))

print(diff)


