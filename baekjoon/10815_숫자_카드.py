# https://www.acmicpc.net/problem/10815
import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

cards.sort()

def binary(start, end, target):
    if start > end:
        return "0"

    mid = (start + end) // 2

    if cards[mid] == target:
        return "1"
    elif cards[mid] > target:
        return binary(start, mid-1, target)
    elif cards[mid] < target:
        return binary(mid+1, end, target)

result = []
for x in arr:
    result.append(binary(0, n-1, x))

print(" ".join(result))




