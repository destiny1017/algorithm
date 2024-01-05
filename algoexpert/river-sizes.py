# https://www.algoexpert.io/questions/river-sizes
# solved with DFS

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def riverSizes(matrix):
    rivers = []
    # Write your code here.
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                rivers.append(dfs(i, j, matrix, 0))
    return rivers


def dfs(n, m, matrix, cnt):
    matrix[n][m] = 0
    cnt += 1

    for i in range(4):
        nx = dx[i] + n
        ny = dy[i] + m

        if nx < 0 or nx >= len(matrix) or ny < 0 or ny >= len(matrix[0]):
            continue
        if matrix[nx][ny] == 0:
            continue
        cnt = dfs(nx, ny, matrix, cnt)

    return cnt
