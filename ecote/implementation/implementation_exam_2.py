# 시간
# 60초 -> 3 13 23 30~39(10) 43 53 == 15개
# 60분 -> (45*15) + (15*60) = 1575개
# 3 13 23시 -> 3600개

n = int(input())
result = 0

for i in range(n+1):
    if i == 3 or i == 13 or i == 23:
        result += 3600
    else:
        result += 1575

print(result)
