

N = int(input())

rtn = [0] * 27
temp = "abcdefghijklmnopqrstuvwxyz"
for _ in range(N):
    s = input()
    for t in range(len(temp)):
        if s[0] == temp[t]:
            rtn[t] += 1

for i in range(len(temp)):
    if rtn[i] > 4:
        print(temp[i], end="")
if max(rtn) < 5:
    print("PREDAJA")