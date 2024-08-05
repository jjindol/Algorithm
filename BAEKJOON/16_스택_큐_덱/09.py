import sys
input = sys.stdin.readline
from collections import deque

q = deque()

def push_front(X):
    q.appendleft(X)
    
def push_back(X):
    q.append(X)
    
def pop_front():
    if q:
        return q.popleft()
    return -1

def pop_back():
    if q:
        return q.pop()
    return -1

def size():
    return len(q)

def isEmpty():
    if not q:
        return 1
    return 0

def print_front():
    if q:
        return q[0]
    return -1

def print_back():
    if q:
        return q[-1]
    return -1

n = int(input())

for i in range(n):
    command = input().split()
    num = command[0]
    
    if num == '1':
        push_front(command[1])
        
    elif num == '2':
        push_back(command[1])
        
    elif num == '3':
        print(pop_front())
        
    elif num == '4':
        print(pop_back())
        
    elif num == '5':
        print(size())
        
    elif num == '6':
        print(isEmpty())
        
    elif num == '7':
        print(print_front())
        
    elif num == '8':
        print(print_back())