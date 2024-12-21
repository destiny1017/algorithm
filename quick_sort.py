def quick_sort(arr, start, end):
    if start >= end:
        return

    # 첫번째 요소를 pivot으로 선정
    pivot = start

    # pivot 바로 다음 요소를 시작점으로
    left = start + 1
    right = end

    # left가 right보다 같거나 커지면 pivot 기준 좌우 정렬이 끝났다는 뜻
    while left <= right:
        # pivot보다 큰 요소를 찾을 때까지 오른쪽으로 이동
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # pivot보다 작은 요소를 찾을 때까지 왼쪽으로 이동
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if right < left:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

arr = [5,7,9,0,3,1,6,2,4,8]
print(arr)
quick_sort(arr, 0, len(arr)-1)
print(arr)