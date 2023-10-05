import sys

t = int(sys.stdin.readline())
site = [None] * t
cnt = 0

for i in range(t):
    site[i] = tuple(map(int, sys.stdin.readline().split()))

def combination(n, m, min, max):
    print(n, m)
    if n == min:
        global cnt
        cnt += 1
        return

    for i in range(n, max - (min - n)):
        combination(n+1, i, min, max)

    # for i in range(n, min+1):
    #     for j in range(i, m+1):
    #         combination(n+1, j, min, max)



for i in range(t):
    cnt = 0
    n, m = site[i]
    combination(1, m, n, m)
    print(cnt)

