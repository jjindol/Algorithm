t = int(input())

for _ in range(t):
    r,s = map(str, input().split())
    r = int(r)

    for x in s:
        print(x * r, end="")
    print()