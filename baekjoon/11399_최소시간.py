n = int(input())

a = list(map(int, input().split()))

a.sort()

total_time = 0
temp = 0
for i in a:
    temp += i
    total_time += temp

print(total_time)
