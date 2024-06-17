n = int(input())
d = dict()

for _ in range(n):
    book = input()
    if book not in d:
        d[book] = 1
    else:
        d[book] += 1

max_val = max(d.values())
result = []

for x,y in d.items():
    if y == max_val:
        result.append(x)
result.sort()
print(result[0])