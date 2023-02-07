
S = input()
print(int(S[::-1] == S))

# if len(S) % 2 != 0:
#     mid = int(len(S)/2 - 1)
# else :
#     mid = int(len(S) / 2)
# temp = 1
# for s in range(0, mid):
#     if S[s] == S[s-temp]:
#         temp += 2
#         continue
#     else:
#         print("0")
#         temp = 0
#         break
# if temp != 0:
#     print("1")
