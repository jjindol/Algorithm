from itertools import product

n,m = map(int, input().split())
lst = []

for i in range(1,n+1):
    lst.append(i)
tmp = product(lst, repeat=m)

for x in tmp:
    print(*x)