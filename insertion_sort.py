
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
    return arr

arr = [8,5,1,6,9,2,4,5]
print(insertion_sort(arr))