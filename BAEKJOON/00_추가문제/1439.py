s = input()

cnt_0 = 0
cnt_1 = 0

if s[0] == '0':
    cnt_0 += 1
else:
    cnt_1 += 1

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == '0':
            cnt_0 += 1
        else:
            cnt_1 += 1

if cnt_0 > cnt_1:
    key = cnt_1
elif cnt_0 < cnt_1:
    key = cnt_0

if '1' not in s or '0' not in s:
    print(0)
elif cnt_0 == cnt_1:
    print(cnt_0)
elif cnt_0 != cnt_1:
    print(key)