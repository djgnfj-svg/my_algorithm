
'''
1. n을 계속 곱해서 모든자리수가 1인경우를 찾는다.
2. 그 수의 자릿수를 출력한다.
'''



while True:
    try :
        a = int(input())
    except :
        break
    temp = 0
    i = 1
    while True:
        temp = temp * 10 + 1
        temp %= a
        if temp== 0:
            print(i)
            break
        i += 1


