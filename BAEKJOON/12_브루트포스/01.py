n,m = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            tmp = nums[i] + nums[j] + nums[k]
            if tmp <= m:
                result = max(result, tmp)

print(result)