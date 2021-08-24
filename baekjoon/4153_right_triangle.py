while True:
    num = list(map(int, input().split()))
    k = max(num)
    if sum(num) == 0:
        break

    num.remove(k)
    if num[0]**2 + num[1]**2 == k**2:
        print("right")

    else:
        print("wrong")

