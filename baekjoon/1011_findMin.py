#규칙 파악이 관 건..

from math import sqrt

for tc in range(int(input())):
    x, y = map(int, input().split())

    distance = y-x

    if distance <= 3:
        print(distance)

    else:
        n = int(sqrt(y-x))

        if distance == n**2:
            print(2*n-1)
        elif n**2 < distance <= n**2 + n :
            print(2*n)
        elif n**2 +n < distance <= n**2 + 2*n:
            print(2*n+1)

