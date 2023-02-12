
n = int(input())

num = 0
for n in range(n):
    str = input()
    temp = []
    for s in str:
        if temp:
            if s == temp[-1]:
                temp.pop()
            else:
                temp.append(s)
        else :
            temp.append(s)
    if not temp:
        num += 1
print(num)

            