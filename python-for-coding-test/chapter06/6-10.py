n = int(input())
lst = []

for i in range(n):
    num = int(input())
    lst.append(num)

lst.sort(reverse=True)

for x in lst:
    print(x, end=' ')