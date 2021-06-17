alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = input()

for i in alphabet:
    word = word.replace(i, '*')  # replace 를 통해 변환.  Replace 를 알면 쉽게 풀 수 있음...


print(len(word))



