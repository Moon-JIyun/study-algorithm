a, b = input().split()

a = a[::-1]  #문자열을 뒤집는 방법 [ :: -1]
b = b[::-1]

if a > b:
    print(a)
else:
    print(b)