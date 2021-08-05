m = int(input())
n = int(input())

prime_num = []
for i in range(m, n+1):
    check = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                check += 1
                break
            else:
                continue
        if check == 0 :
            prime_num.append(i)



if len(prime_num) > 0:
    print(sum(prime_num))
    print(min(prime_num))

else:
    print(-1)


