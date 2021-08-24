check = [False, False] + [True]*10002

k = int(10002 ** 0.5)

for i in range(2, k+1):
    if check[i] == True:
        for j in range(i+i, 10001, i):
            check[j] = False


T = int(input())

for tc in range(T):
    n = int(input())

    a = n//2
    b = a
    for i in range(10000):
        if check[a] and check[b]:
            print(a, b)
            break
        a -= 1
        b += 1
# 주어진 n 을 2로 나누어 a, b 가 모두 소수면 그대로 반환, 소수가 아닐 시, a를 1씩 줄여가고 b를 1씩 키워가며 소수 확인