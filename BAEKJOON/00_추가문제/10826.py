import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def f(n):
    if n==0:
        return 0
    
    dp = [0]*(n+1)
    dp[1] = 1
    
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
        
    return dp[n]

n = int(input())
print(f(n))