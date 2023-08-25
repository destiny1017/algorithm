
chars = list(input())

strs = []
num = 0

for i in chars:
    if i.isalpha():
        strs.append(i)
    else:
        num += int(i)

strs.sort()

if num > 0:
    strs.append(str(num))

print(''.join(strs))


