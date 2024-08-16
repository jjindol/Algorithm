n = int(input())
num = list(map(int, input().split()))


def move(x):
    lst = []
    for i in range(1,n+1):
        tmp = abs(i-x)
        lst.append(tmp)
    
    sum = 0
    for j in range(n):
        sum += lst[j] * num[j]

    return sum

min = float('inf')

for x in range(1,n+1):
    result = move(x)
    if result < min:
        min = result

print(min)