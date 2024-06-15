# word = "Mississipi"
# lower_case = word.lower()
# s_count = lower_case.count("s")
# print(s_count)

word = input().upper()
word_list = list(set(word))
cnt = []

for x in word_list:
    count = word.count(x)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[cnt.index(max(cnt))])