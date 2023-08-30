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


# 퀵정렬2

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

print("정렬 전 : ", arr)


def quick(array):
    if len(array) <= 1:
        return array

    left_arr, mid_arr, right_arr = [], [], []
    pivot = array[len(array) // 2]

    for i in array:
        if pivot > i:
            left_arr.append(i)
        elif pivot < i:
            right_arr.append(i)
        else:
            mid_arr.append(i)

    return quick(left_arr) + mid_arr + quick(right_arr)


print("정렬 후 : ", quick(arr))
