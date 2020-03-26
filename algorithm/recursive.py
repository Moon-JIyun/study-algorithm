#w재귀 함수 -> sum // 피보나치 ,하노이 탑 등 사용

#countdown
def countdown(n):
    if n == 0:
        print("BOOM!!")
    else:
        print(n)
        countdown(n-1)
    return

#재귀 함수로 구구단 출력
def multiply(x, n):
    if n==0:
        print('end')
    else:
        multiply(x, n-1)
        print('{}X{} = {}'.format(x,n,x*n))
    return

#factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#   