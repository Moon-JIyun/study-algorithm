words = list(map(str, input().split(" ")))
while "" in words:
    words.remove("")
print(len(words))
