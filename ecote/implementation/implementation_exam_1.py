# 상하좌우 문제

# 북동남서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
directions = ['U', 'R', 'D', 'L']
x, y = 1, 1

n = int(input())
data = list(input().split())

for d in data:
    nx = x + dx[directions.index(d)]
    ny = y + dy[directions.index(d)]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    x, y = nx, ny

print(x, y)



