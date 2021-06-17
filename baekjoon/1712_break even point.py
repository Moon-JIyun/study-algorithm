a, b, c = map(int, input().split(" "))

if c <= b:
    print(-1)
else:
    N = a // (c-b) +1
    print(N)





