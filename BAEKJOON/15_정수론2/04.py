import math
from functools import reduce

n = int(input())
lst = []

for _ in range(n):
    x = int(input())
    lst.append(x)

lst2 = []
for i in range(n-1):
    tmp = lst[i+1] - lst[i]
    lst2.append(tmp)

# lst2의 모든 요소에 대해 gcd 계산
a = reduce(math.gcd, lst2)
b = (max(lst) - min(lst))//a + 1

print(b-len(lst))