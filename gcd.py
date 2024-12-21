def gcd_recursive(n, m):
    print(n, m)
    if m == 0:
        return n
    return gcd_recursive(m, n % m)

def gcd_loop(n, m):
    num = sorted([n, m])
    for i in range(num[0], 0, -1):
        if num[1] % i == 0 and num[0] % i == 0:
            return i
    return 1

n1, m1 = 27, 15
n2, m2 = 25, 14
print(gcd_recursive(n1, m1))
print(gcd_recursive(n2, m2))
print(gcd_loop(n1, m1))
print(gcd_loop(n2, m2))
