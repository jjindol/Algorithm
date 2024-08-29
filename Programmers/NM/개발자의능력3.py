nums = list(map(int, input().split()))

def func(i,j,k):
    sum1 = nums[i]+nums[j]+nums[k]
    sum2 = sum(nums) - sum1
    return abs(sum1-sum2)

result = 100
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1,6):
            result = min(func(i,j,k), result)

print(result)