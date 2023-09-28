import sys
from collections import deque
import copy
from itertools import combinations

sys.setrecursionlimit(10 ** 6)

n, m = map(int, sys.stdin.readline().split())
board = []
cnt = 0
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
wall_able = []
virus = deque()
max_safe_count = 0
safe_cnt = 0

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

# 바이러스 좌표 구하기
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus.append((i, j))

# 안전 영역 개수 구하기
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            safe_cnt += 1
            wall_able.append((i, j))

# 안전 영역에서 추가되는 벽 개수만큼 빼기
safe_cnt -= 3


def bfs(road, queue):
    global safe_cnt
    global max_safe_count
    safe = safe_cnt

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if n <= nx or nx < 0 or m <= ny or ny < 0:
                continue
            if road[nx][ny] != 0:
                continue

            safe -= 1
            if safe < max_safe_count:
                return
            road[nx][ny] = 3
            queue.append((nx, ny))

    max_safe_count = max(max_safe_count, safe)


# 3개의 벽 설치가 가능한 모든 경우의 수 구하기
wall_combinations = combinations(wall_able, 3)

# 벽 설치 경우의 수만큼 bfs 수행
for wall in wall_combinations:
    road = copy.deepcopy(board)
    queue = copy.deepcopy(virus)
    for x, y in wall:
        road[x][y] = 1

    bfs(road, queue)

print(max_safe_count)
