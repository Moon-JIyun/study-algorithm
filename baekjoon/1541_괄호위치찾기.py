x = input().split('-')
num = []
for i in x:
    cnt = 0
    y = i.split('+')
    for j in y:
        cnt += int(j)
    num.append(cnt)

n = num[0]
for k in range(1, len(num)):
    n -= num[k]

print(n)




