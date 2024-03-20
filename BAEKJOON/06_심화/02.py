#방법1
num = [1,1,2,2,2,8]
a,b,c,d,e,f = map(int, input().split())

result = num[0]-a, num[1]-b, num[2]-c, num[3]-d, num[4]-e, num[5]-f
print(*result)



# 방법2
num = [1, 1, 2, 2, 2, 8]
values = list(map(int, input().split()))

result = []
for i in range(len(num)):
    result.append(num[i] - values[i])

print(*result)