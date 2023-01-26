

temp = []
for i in range(10):
    temp.append(int(input()))

sum = 0
for j in temp:
    if abs(sum + j - 100) > abs(sum - 100):
        break
    sum += j
print(sum)