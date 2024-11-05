# dp를 이용한 풀이
def solution(x):
    dp = [-1]*(x+1)
    
    if x >= 3:
        dp[3] = 1
    if x >= 5:
        dp[5] = 1
        
    for i in range(6,x+1):
        if dp[i-3] != -1:
            dp[i] = dp[i-3]+1
        if dp[i-5] != -1:
            if dp[i] == -1:
                dp[i] = dp[i-5]+1
            else:
                dp[i] = min(dp[i], dp[i-5]+1)
                
        return dp[x]
    
print(solution(int(input())))

''' 반복문을 이용한 풀이
n = int(input())

cnt = 0
while n>=0:
    if n%5==0:
        cnt += (n//5)
        print(cnt)
        break
    n -= 3
    cnt += 1
else:
    print(-1)
'''