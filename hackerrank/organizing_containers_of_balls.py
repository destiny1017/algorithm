#!/bin/python3
# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # 컨테이너 수와 공 수를 담을 리스트 초기화
    size_of_containers = [0] * len(container)
    numbers_of_balls = [0] * len(container[0])

    # 각 컨테이너 수와 각 공의 수를 계산
    for i in range(len(container)):
        size_of_containers[i] = sum(container[i])
        for j in range(len(container[i])):
            numbers_of_balls[j] += container[i][j]

    # 공 배열과 컨테이너 배열을 정렬하여 동일성 비교하여 결과 리턴
    size_of_containers.sort()
    numbers_of_balls.sort()
    return "Possible" if size_of_containers == numbers_of_balls else "Impossible"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        # fptr.write(result + '\n')

    # fptr.close()
