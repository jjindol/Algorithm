import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

lst = []
for i in range(n):
    word = input()
    if len(word) > m:
        lst.append(word)

d = dict()
for word in lst:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

result = sorted(d.keys(), key=lambda x: (-d[x], -len(x), x))

for x in result:
    print(x, end='')