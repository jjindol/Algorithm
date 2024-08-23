n,m = map(int, input().split())
store = int(input())
lst = []

for i in range(store+1):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        lst.append(cmd[1])

    elif cmd[0] == 2:
        lst.append(n + m + (n-cmd[1]))

    elif cmd[0] == 3:
        lst.append(2*n + m + (m-cmd[1]))

    elif cmd[0] == 4:
        lst.append(n + cmd[1])


my_X = lst[-1]
result = 0

for i in range(store):
    distance = abs(my_X - lst[i])
    result += min(distance, 2*(n+m) - distance)

print(result)