import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

lst.sort()

for num in lst:
    print(num)