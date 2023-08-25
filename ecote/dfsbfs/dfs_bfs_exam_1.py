n, m = map(int, input().split())
board = []
result = 0

for i in range(n):
    board.append(list(map(int, input())))


def dfs(x, y):
    if board[x][y] == 1:
        return

    board[x][y] = 1
    if x > 0:
        dfs(x-1, y)
    if x < n-1:
        dfs(x+1, y)
    if y > 0:
        dfs(x, y-1)
    if y < m-1:
        dfs(x, y+1)


for x in range(n):
    for y in range(m):
        if board[x][y] == 0:
            dfs(x, y)
            result += 1

print(result)

