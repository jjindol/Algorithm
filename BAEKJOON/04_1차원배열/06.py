import sys
n,m = map(int, input().split())

basket = []
for a in range(1, n+1):
    basket.append(a)

for _ in range(m):
    i,j= map(int, sys.stdin.readline().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)