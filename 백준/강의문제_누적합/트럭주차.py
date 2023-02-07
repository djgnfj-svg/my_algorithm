import sys

input = sys.stdin.readline

A, B, C  = map(int, input().split())

rtn = [0] * 100
for i in range(0,3):
    a, b = map(int, input().split())
    for j in range(a, b):
        rtn[j] += 1


sum = 0
for i in rtn:
    if i == 1:
        sum += i * A
    elif i == 2:
        sum += i * B
    elif i == 3:
        sum += i * C
print(sum)