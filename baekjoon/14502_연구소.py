import sys
from collections import deque
import copy

sys.setrecursionlimit(10 ** 6)

n, m = map(int, sys.stdin.readline().split())
board = []
cnt = 0
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
max_safe_count = 0

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))


def print_road(road):
    for i in range(n):
        print(road[i])
    print("------------------------")


def bfs(road, queue):
    while len(queue) > 0:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # print(nx, ny)
            if n <= nx or nx < 0 or m <= ny or ny < 0:
                # print(nx, ny, "continued")
                continue
            if road[nx][ny] != 0:
                continue
            road[nx][ny] = 3
            queue.append((nx, ny))


def safe_count(road):
    global max_safe_count
    safe_cnt = 0
    for i in range(n):
        for j in range(m):
            if road[i][j] == 0:
                safe_cnt += 1
    if max_safe_count < safe_cnt:
        max_safe_count = safe_cnt


def contagion(road):
    for i in range(n):
        for j in range(m):
            if road[i][j] == 2:
                queue = deque()
                queue.append((i, j))
                bfs(road, queue)
    return safe_count(road)


def rounds(road, depth):
    for i in range(n):
        for j in range(m):
            if road[i][j] != 1 and road[i][j] != 2:
                if depth < 3:
                    road[i][j] = 1
                    if depth == 2:
                        # print_road(road)
                        contagion(copy.deepcopy(road))
                        # print(safe_count)
                        # global cnt
                        # cnt += 1
                    rounds(road, depth + 1)
                    road[i][j] = 0


rounds(board, 0)
print(max_safe_count)
