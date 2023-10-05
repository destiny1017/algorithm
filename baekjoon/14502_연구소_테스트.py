import sys
from collections import deque
from itertools import combinations
import time

n, m = map(int, sys.stdin.readline().split())
board = []
max_safe_count = 0

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))


def bfs():
    temp_board = [row[:] for row in board]
    queue = deque()

    for i in range(n):
        for j in range(m):
            if temp_board[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and temp_board[nx][ny] == 0:
                temp_board[nx][ny] = 2
                queue.append((nx, ny))

    safe_count = sum(row.count(0) for row in temp_board)
    return safe_count


# 벽을 설치할 수 있는 후보 위치를 미리 계산
empty_spaces = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 0]

st = time.time()
# 조합을 사용하여 벽을 설치할 위치 선택
wall_combinations = combinations(empty_spaces, 3)
# print(len(list(wall_combinations)))

for walls in wall_combinations:
    for x, y in walls:
        board[x][y] = 1

    safe_count = bfs()
    max_safe_count = max(max_safe_count, safe_count)

    for x, y in walls:
        board[x][y] = 0


ed = time.time()
print(max_safe_count)
print(f"{ed - st:.5f} sec")

