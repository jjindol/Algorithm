n = int(input())
s = set()

for _ in range(n):
    word = input()
    s.add(word)

for x in s:
    if x[::-1] in s:
        break

print(len(x), x[(len(x) - 1) // 2])