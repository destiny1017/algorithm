# 효율적인 화폐 구성

n, m = map(int, input().split())
money = [0] * n
dp = [-1] * (m + 1)

for i in range(n):
    money[i] = int(input())

for i in range(1, m+1):
    for j in range(len(money)-1, -1, -1):
        if dp[i] == -1 and i % money[j] == 0:
            dp[i] = i // money[j]
        if i > money[j] and dp[i - money[j]] > -1:
            if dp[i] == -1:
                dp[i] = dp[i - money[j]] + 1
            else:
                dp[i] = min(dp[i - money[j]] + 1, dp[i])

# print(dp[:m+1])
print(dp[m])
