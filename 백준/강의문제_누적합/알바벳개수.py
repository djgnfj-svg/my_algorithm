import sys
input = sys.stdin.readline

S = input()

rtn = "abcdefghijklmnopqrstuvwxyz"
for r in rtn:
    sum = 0
    for s in S:
        if r == s:
           sum += 1
    print(sum, end=" ")
