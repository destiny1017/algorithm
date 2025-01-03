# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    ar = A % K
    br = B % K
    a,b = A,B
    if ar > 0:
        a = K - ar + A
    if br > 0:
        b = B - br

    return (b - a) // K + 1