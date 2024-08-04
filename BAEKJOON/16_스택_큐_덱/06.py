import sys
input = sys.stdin.readline
from collections import deque
q = deque()

def push(x):
    q.append(x)

def pop():
    if not q:
        return -1
    return q.popleft()

def size():
    return len(q)

def empty():
    if not q:
        return 1
    return 0

def front():
    if not q:
        return -1
    return q[0]

def back():
    if not q:
        return -1
    return q[-1]


n = int(input())
for i in range(n):
    command = input().split()

    if command[0] == 'push':
        push(command[1])

    elif command[0] == 'pop':
        print(pop())

    elif command[0] == 'size':
        print(size())

    elif command[0] == 'empty':
        print(empty())

    elif command[0] == 'front':
        print(front())

    elif command[0] == 'back':
        print(back())