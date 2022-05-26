n = int(input())

time_table = []
for i in range(n):
    start, finish = map(int, input().split())
    a = (start, finish)
    time_table.append(a)

time_table.sort(key = lambda x:(x[1],x[0]))

count = 1
end_time = time_table[0][1]
for i in range(0, n-1):
    if end_time <= time_table[i+1][0]:
        count +=1
        end_time = time_table[i+1][1]

print(count)

