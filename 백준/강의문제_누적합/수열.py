

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
list_temp = list(map(int, input().split()))

temp = []
temp.append(sum(list_temp[:K]))
for n in range(N-K):
    temp.append(temp[n] - list_temp[n] + list_temp[n+K])

print(max(temp))