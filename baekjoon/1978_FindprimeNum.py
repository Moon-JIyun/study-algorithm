T = int(input())
num = list(map(int, input().split()))

count = 0

for i in num:
    nonePrimenum = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                nonePrimenum += 1
        if nonePrimenum == 0:
            count +=1
