
def fibonacci_dp(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-2] + dp[i-1])
    print(dp)
    return dp[n]

def fibonacci_recursive(n):
    if n <= 2:
        return 1

    return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)

print(fibonacci_dp(10))
print(fibonacci_recursive(10))
