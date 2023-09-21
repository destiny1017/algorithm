# 정렬된 배열에서 특정 수의 개수 구하기
'''
테스트 데이터
7 2
1 1 2 2 2 2 3

13 3
1 1 1 2 3 3 3 3 3 3 4 4 5

17 5
1 1 2 2 2 2 2 2 2 2 2 2 2 2 3 4 5

17 0
1 1 2 2 2 2 2 2 2 2 2 2 2 2 3 4 5

17 6
1 1 2 2 2 2 2 2 2 2 2 2 2 2 3 4 5

'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def binary_min(start, end, target):
    # print("start=%d, end=%d" % (start, end))
    if start >= end:
        # print("start is ", start)
        return start

    mid = (start + end) // 2

    if arr[mid] > target:
        return binary_min(start, mid-1, target)
    elif arr[mid] < target:
        return binary_min(mid+1, end, target)
    else:
        if arr[mid-1] < target:
            # print("start is ", mid)
            return mid
        else:
            return binary_min(start, mid-1, target)


def binary_max(start, end, target):
    # print("start=%d, end=%d" % (start, end))
    if start >= end:
        # print("end is ", start)
        return start

    mid = (start + end) // 2

    if arr[mid] > target:
        return binary_max(start, mid - 1, target)
    elif arr[mid] < target:
        return binary_max(mid+1, end, target)
    else:
        if arr[mid+1] > target:
            # print("end is ", mid)
            return mid
        else:
            return binary_max(mid+1, end, target)


if m < arr[0] or m > arr[n-1]:
    print(-1)
else:
    left = binary_min(0, n-1, m)
    right = binary_max(left, n-1, m)
    print(right - left + 1)
