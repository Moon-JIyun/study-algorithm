def hanoi(n, start, arrive):
    if n == 1:
        print(start, arrive)
        return

    hanoi(n-1, start, 6-start-arrive)
    print(start, arrive)
    hanoi(n-1, 6-start-arrive, arrive)



n = int(input())

print(2**n-1)
hanoi(n, 1, 3)