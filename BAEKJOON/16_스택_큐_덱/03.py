t = int(input())

for i in range(t):
    stack = []
    s = input()
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                print('NO')
                break
            stack.pop()
            
    else:
        if not stack:
            print('YES')
        else:
            print('NO')