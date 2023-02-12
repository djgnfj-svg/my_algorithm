
#내답
S = str(input())

al = 'abcdefghijklmnopqrstuvwxyz'
for a in al:
    num = 0
    for s in S:
        if s == a:
           num += 1 

    print(num, end=" ")

# 더좋은답
# s = input()
# la = [0] * 26
# for i in s:
#     la[ord(i)-97] += 1
# print(*la)