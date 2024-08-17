MAX_NUM = 10002
arr = [0]*MAX_NUM

n,k = map(int, input().split())

for i in range(n):
    num, cmd = input().split()
    num = int(num)

    if cmd == 'G':
        cmd = 1
    elif cmd == 'H':
        cmd = 2

    arr[num] = cmd


tmp = sum(arr[1:k+2])
result = tmp

for i in range(k,MAX_NUM-2):
    tmp = tmp - arr[i-k+1] + arr[i+1]
    result = max(result, tmp)

print(result)