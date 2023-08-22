# 모험가 길드

n = int(input())
data = list(map(int, input().split()))

data.sort()

member = 0
team = 0

for fear in data:
    member += 1
    if member >= fear:
        team += 1
        member = 0

print(team)
