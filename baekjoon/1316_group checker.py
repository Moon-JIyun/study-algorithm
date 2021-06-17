count = 0
for tc in range(int(input())):
    word = input()
    check = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new_word = word[i+1:]
            if new_word.count(word[i]) > 0:
                check += 1
    if check == 0:
        count += 1

print(count)


# short coding
cnt = 0
for i in range(int(input())):
    a = input()
    if list(a) == sorted(a, key=a.find):
        cnt += 1
print(cnt)


# if list(word) == sorted(word, key=word.find):
# 파이썬의 내장 함수인 sorted() 함수는 key라는 인수로 함수를 전달받아, 해당 함수를 실행한 결과값을 기준으로 정렬을 진행하게 됩니다.



