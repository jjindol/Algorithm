import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    x = list(map(int, input().split()))

    #push
    if x[0]==1:
        stack.append(x[1])

    #pop
    elif x[0]==2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    #size
    elif x[0]==3:
        print(len(stack))

    #empty
    elif x[0]==4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    #top
    elif x[0]==5:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])