# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    binstr = bin(N)[2:]
    result = 0
    flag = False
    cnt = 0
    for i in range(len(binstr)):
        if binstr[i] == '1':
            if flag:
                result = max(result, cnt)
                cnt = 0
            else:
                flag = True
        else:
            if flag:
                cnt += 1
    return result