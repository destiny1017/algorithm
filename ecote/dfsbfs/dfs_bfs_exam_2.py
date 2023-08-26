# 미로탈출
from collections import deque

n, m = map(int, input().split())
board = []
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    board.append(list(map(int, input())))

queue = deque()

def bfs():
    queue.append((0, 0))
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            kx = nx + dx[i]
            ky = ny + dy[i]
            if n <= kx or kx < 0 or m <= ky or ky < 0:
                continue
            # print(kx, ky)
            if board[kx][ky] == 0:
                continue

            if board[kx][ky] == 1:
                board[kx][ky] = board[nx][ny] + 1
                queue.append((kx, ky))

bfs()
print(board[n-1][m-1])
