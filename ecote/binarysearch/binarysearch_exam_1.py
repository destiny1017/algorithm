n, k = map(int, input().split())
arr = list(map(int, input().split()))


def binary_search(start, end, target):

    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(mid+1, end, target)
    else:
        return binary_search(start, mid-1, target)


result = binary_search(0, n-1, k)

if result == None:
    print("찾으려는 값이 존재하지 않습니다.")
else:
    print(result)

