import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    x = int(input())
    if x!=0:
        stack.append(x)
    elif x==0:
        stack.pop()

print(sum(stack))