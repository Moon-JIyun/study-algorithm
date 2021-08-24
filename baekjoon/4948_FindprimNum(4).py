# n = int(input())
#
# prime_num = []
# for i in range(n+1, 2*n+1):
#     check = 0
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 check += 1
#                 break
#             else:
#                 continue
#         if check == 0 :
#             prime_num.append(i)
#
# print(len(prime_num))
#  위 코드는 시간 초과.

# 1 < n < 123,456

def PrimeNum(n):
    a = int(n**0.5)
    if n == 1:
        return False
    else:
        for i in range(2, a+1):
            if n % i == 0:
                return False
        return True

num_list = list(range(2, 246912))
sort_list = []

for i in num_list:
    if PrimeNum(i):
        sort_list.append(i)

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in sort_list:
        if n < i <= n*2:
            cnt += 1
    print(cnt)

