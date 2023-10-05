# https://www.acmicpc.net/problem/2468
import sys
from collections import deque

n = int(sys.stdin.readline())
frame = []
flooded = []
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

max_height = 0
min_height = 100
max_safe_zone = 0

for i in range(n):
    frame.append(list(map(int, sys.stdin.readline().split())))

for row in frame:
    max_height = max(max_height, max(row))
    min_height = min(min_height, min(row))


def bfs(px, py):
    queue = deque()
    queue.append((px, py))
    flooded[px][py] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx >= n or nx < 0 or ny >= n or ny < 0 or flooded[nx][ny]:
                continue
            flooded[nx][ny] = True
            queue.append((nx, ny))


for water_depth in range(0, max_height):
    flooded = [[False] * n for _ in range(n)]
    safe_zone = 0

    for i in range(n):
        for j in range(n):
            if water_depth >= frame[i][j]:
                flooded[i][j] = True

    for i in range(n):
        for j in range(n):
            if not flooded[i][j]:
                bfs(i, j)
                safe_zone += 1

    # print(f"depth = {water_depth}, safe zone = {safe_zone}")
    max_safe_zone = max(max_safe_zone, safe_zone)


print(max_safe_zone)
