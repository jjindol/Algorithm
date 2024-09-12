t = int(input())

MAX = 10001
dp = [0] * MAX

dp[1] = 1
dp[2] = 1

for i in range(3,MAX):
    dp[i] = dp[i-1] + dp[i-2]
    
for i in range(1,t+1):
    x,y = map(int, input().split())
    
    print("Case #" + str(i) + ":", dp[x] % y)