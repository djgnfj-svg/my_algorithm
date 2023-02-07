
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

temp = [list(map(int, input().split())) for _ in range(N)]
dp1 = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        dp1[i][j] = dp1[i][j-1]+ dp1[i-1][j] - dp1[i-1][j-1] + temp[i-1][j-1]
        print(dp1)
print(dp1)
print("---------------------")

dp2 = [[0] * (N+1)] * (N+1)
for i in range(1, N+1):
    for j in range(1, N+1):
        dp2[i][j] = dp2[i][j-1]+ dp2[i-1][j] - dp2[i-1][j-1] + temp[i-1][j-1]
        print(dp2)
print(dp2)

# for m in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     print(dp[x2][y2] - dp[x1][x2-1] - dp[x1-1][x2-1] + dp[x1-1][x2-1])
