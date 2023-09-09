# 떡볶이 떡 만들기
# 테스트 데이터
'''
4 6
19 15 10 17
'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

def binary_search(start, end, target):
    if start > end:
        return end

    mid = (start + end) // 2

    sum = 0
    for i in arr:
        if i <= mid:
            break
        else:
            sum += i - mid

    print(mid, sum)
    if sum == target:
        return mid
    elif sum < target:
        return binary_search(start, mid-1, target)
    elif sum > target:
        return binary_search(mid+1, end, target)


result = binary_search(0, arr[0], m)
print(result)
