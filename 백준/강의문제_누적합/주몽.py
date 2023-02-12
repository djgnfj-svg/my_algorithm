
import sys

input = sys.stdin.readline
N = int(input())
M = int(input())

cnt = 0
temp = list(map(int, input().split()))

letf = 0
right = N-1
temp.sort()
while letf < right:
    if temp[letf] + temp[right] == M:
        cnt += 1
        letf += 1
        right -= 1
    elif temp[letf] + temp[right] < M:
        letf += 1
    elif temp[letf] + temp[right] > M:
        right -= 1
print(cnt)