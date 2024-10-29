import sys,math
input = sys.stdin.readline

n,m = map(int, input().split())
comb = math.factorial(n) // (math.factorial(m) * math.factorial(n-m))

remainder = 0
cnt = 0
while remainder == 0:
    remainder = comb % 10
    
    if remainder == 0:
        cnt += 1

    comb = comb // 10

print(cnt)

#시간 초과