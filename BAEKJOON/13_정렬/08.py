import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    x,y = map(int, input().split())
    lst.append((x,y))

lst.sort(key=lambda m : (m[1], m[0]))

for num in lst:
    print(num[0], num[1])