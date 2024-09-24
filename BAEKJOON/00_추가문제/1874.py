n = int(input())
stack = []
lst = []
start = 1

for _ in range(n):
    end = int(input())
    while start <= end:
        stack.append(start)
        lst.append('+')
        start += 1

    if stack[-1] == end:
        stack.pop()
        lst.append('-')
    else:
        print('NO')
        break
else:
    for i in lst:
        print(i)