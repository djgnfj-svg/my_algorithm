from sys import stdin
N = int(input())

pattern = stdin.readline().rstrip()
p = pattern.split("*")
p1, p2 = p[0], p[1]
for n in range(N):
    s = input()
    print(f"join차이 일반 : {len(p)} | {len(''.join(p))}")
    if s[:len(p1)] == p1 and s[-len(p2):] == p2 and len(''.join(p)) <= len(s):
        print("DA")
    else:
        print("NE")