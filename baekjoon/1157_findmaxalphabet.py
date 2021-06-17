word = input().upper()
set_word = list(set(word))
cnt_list = []

for i in set_word:
    cnt = word.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
    print("?")
else:
    max_idx = cnt_list.index(max(cnt_list))
    print(set_word[max_idx])


