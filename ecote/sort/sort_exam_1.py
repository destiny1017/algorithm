# 버블정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

print("정렬 전 : ", arr)

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if(arr[j] > arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("정렬 후 : ", arr)

