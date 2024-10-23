import sys
input = sys.stdin.readline

def func(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            return False
    return True

n = int(input())
cnt = 0
for _ in range(n):
    x = input()
    if func(x):
        cnt += 1
print(cnt)