n, k = map(int, input().split())
coins = []

for i in range(n):
    a = int(input())
    coins.append(a)

coins.sort(reverse=True)

count = 0
for coin in coins:
    count = count + k // coin
    k = k % coin

print(count)