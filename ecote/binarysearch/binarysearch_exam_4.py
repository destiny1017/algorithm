# 정렬된 배열에서 특정 수의 개수 구하기
'''
테스트 데이터
7 2
1 1 2 2 2 2 3

13 3
1 1 1 2 3 3 3 3 3 3 4 4 5

17 0
1 1 2 2 2 2 2 2 2 2 2 2 2 2 3 4 5
'''

from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = bisect_right(arr, m) - bisect_left(arr, m)

if count == 0:
    print(-1)
else:
    print(count)

