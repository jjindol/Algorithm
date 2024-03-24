# 방법1
s = input()
alphabet = [i for i in range(97,123)]

for x in alphabet:
    print(s.find(chr(x)), end=" ")


# 방법2
s = input()
alphabet = "abcdefghijklmnopqrstuvwsyz"

for x in alphabet:
    print(s.find(x), end=" ")


# 방법3
my_list = [-1] * 26
s = list(map(ord, input()))

for i in range(len(s)):
    if my_list[s[i]-ord('a')]== -1:
        my_list[s[i]-ord('a')]= i

for i in my_list:
    print(i, end=" ")