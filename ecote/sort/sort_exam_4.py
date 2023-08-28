# 퀵 정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

print("정렬 전 : ", arr)


def quick(start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:

        while left <= end and arr[pivot] >= arr[left]:
            left += 1

        while right > start and arr[pivot] <= arr[right]:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[pivot], arr[right] = arr[right], arr[pivot]

        quick(start, right - 1)
        quick(right+1, end)


quick(0, len(arr)-1)
print("정렬 후 : ", arr)

