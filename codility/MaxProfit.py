# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    sorted_cost = []

    st, ed = 0, 0
    result = 0
    for i in range(len(A)):
        tmp = A[i] - A[st]
        if tmp > result:
            result = tmp
        elif tmp < 0:
            st = i

    return result