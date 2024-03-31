num = []

for _ in range(10):
    x = int(input())
    num.append(x)

unique = set()

for x in num:
    unique.add(x % 42)

print(len(unique))