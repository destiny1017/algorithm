
n = input()
x, y = ord(n[0]) - 97, int(n[1]) - 1
nx = [-2, -1, 1, 2, -2, -1, 1, 2]
ny = [-1, -2, -2, -1, 1, 2, 2, 1]
result = 0

for i in range(8):
    mx = x + nx[i]
    my = y + ny[i]
    if 0 <= mx < 8 and 0 <= my < 8:
        result += 1

print(result)

