#!/bin/python3
# https://www.hackerrank.com/challenges/bigger-is-greater/problem

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

# 1. 역방향으로 탐색하며 지금보다 더 작은 게 나올떄까지 탐색
# 2. 작은 거 발견하면 순회했던 모든 리스트 중 발견한 수와의 차이가 0 이상이면서 가장 적은 거 찾기
# 3. 2에서 찾은 수를 찾은 위치와 변경하고, 변경된 리스트를 오름차순 정렬

def biggerIsGreater(w):
    arr = list(w)
    pivot = -1
    # 뒤에서부터 더 작은 값 찾을 때까지 역순회
    for i in range(len(arr)-1, 0, -1):
        if arr[i] > arr[i-1]:
            pivot = i
            break

    # 더 작은 값 없으면 최대값이므로 no answer 리턴
    if pivot == -1:
        return "no answer"
    else:
        # 기준값의 뒤쪽 값들 중 기준값보다 크면서 기준값과의 차이가 가장 적은 값 찾기
        less_num = 100
        less_num_idx = -1
        target_arr = arr[pivot:]
        for i in range(len(target_arr)):
            if arr[pivot-1] < target_arr[i]:
                less_num = min(less_num, ord(target_arr[i]) - ord(arr[pivot-1]))
                less_num_idx = i

        # 가장 차이가 적은 값을 기준값의 위치와 변경 후 뒤쪽 값들 오름차순 정렬
        arr[pivot-1], arr[pivot+less_num_idx] = arr[pivot+less_num_idx], arr[pivot-1]
        arr[pivot:] = sorted(arr[pivot:])

    return "".join(arr)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)
        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
