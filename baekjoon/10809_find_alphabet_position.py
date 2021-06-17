s = list(map(str, input()))
alpha = list('abcdefghijklmnopqrstuvwxyz')

check = [-1 for i in range(len(alpha))]
for i in range(len(s)):
    if check[alpha.index(s[i])] == -1:
        check[alpha.index(s[i])] = i
for j in check:
    print(j, end =" ")
