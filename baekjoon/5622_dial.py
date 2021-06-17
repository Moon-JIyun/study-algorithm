dial = {
        1: [], 2: ['a','b','c'], 3:['d','e','f'],
        4: ['g','h','i'], 5: ['j','k','l'], 6: ['m','n','o'],
        7: ['p','q','r','s'], 8: ['t','u','v'], 9: ['w','x','y','z']
        }

word = str(input()).lower()
time = 0

for i in range(len(word)):
    for key, value in dial.items():
        if word[i] in value:
            time = time + int(key)+1
print(time)




