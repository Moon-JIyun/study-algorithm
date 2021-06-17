n = int(input())

line = 1
cnt = 1

while True:
    if n < cnt:
        break
    else:
        line += 1
        cnt = cnt + line
if line % 2 ==0:
    upper = n - (cnt-line)
    down = line - upper + 1
else:
    down = n - (cnt -line)
    upper = line - down + 1

print(str(upper) + '/' + str(down))



