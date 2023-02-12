
S = input()

for i in S:
    # 소문자인지 체크
    if i.islower():
        print(chr(97+(ord(i)+13-97)%26), end='')
    # 대문자인지 체크
    elif i.isupper():
        print(chr(65+(ord(i)+13-65)%26), end='')
    else:
        print(i,end='')