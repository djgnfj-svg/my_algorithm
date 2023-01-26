
# 실패했음 시간초과로
# 빠르게 하는 방법을 생각해야됨

input = str(input())
x = 0
s = ""
for i in input:
    if i == "-":
        s = str(s)[::-1]
    else :
        s += i
        x += int(s)

print(x)

