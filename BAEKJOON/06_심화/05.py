word = input().upper()
unique_word = list(set(word))

cnt_list = []
for x in unique_word:
    cnt = word.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_count = max(cnt_list)
    max_index = cnt_list.index(max_count)
    print(unique_word[max_index])


#풀이2
word = input().upper()
unique_word = list(set(word))

cnt_list = [word.count(x) for x in unique_word]
max_count = max(cnt_list)

if cnt_list.count(max_count) > 1:
    print("?")
else:
    most_common_letter = unique_word[cnt_list.index(max_count)]
    print(most_common_letter)
