# 버블정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

print("정렬 전 : ", arr)

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if(arr[j] > arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("정렬 후 : ", arr)


# 선택정렬
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)


# 삽입정렬
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

print(arr)

