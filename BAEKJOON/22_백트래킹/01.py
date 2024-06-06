from itertools import permutations

n,m = map(int, input().split())
lst = []

for i in range(1,n+1):
    lst.append(i)
tmp = permutations(lst, m)
for x in tmp:
    print(*x)