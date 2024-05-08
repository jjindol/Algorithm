x = int(input())
num = list(map(int, input().split()))
result = 0

for i in range(len(num)):
    count = 0
    for j in range(1, num[i]+1):
        if (num[i]%j) == 0:
            count += 1
    if count == 2:
        result += 1
print(result)