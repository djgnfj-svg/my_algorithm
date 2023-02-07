import sys
import itertools

input = sys.stdin.readline
rtn = []
for i in range(0,9):
    rtn.append(int(input()))

rtn.sort()

for i in itertools.combinations(rtn, 7):
    if sum(i) == 100 :
        for j in sorted(i):
            print(j)
        break