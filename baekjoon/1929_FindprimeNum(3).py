m,n = map(int, input().split(" "))

prime_num = [True] * (n+1)
prime_num[0] = False
prime_num[1] = False

k = int(n ** 0.5)

for i in range(2,k+1):
    if prime_num[i] == True:
        for j in range(i+i,len(prime_num),i):
            prime_num[j] = False

for i in range(m,n+1):
    if prime_num[i] == True:
        print(i)
