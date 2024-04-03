#시간초과 코드
import sys
input = sys.stdin.readline
a,b,v = map(int, input().split())
n = 0

while a*n - b*(n-1) < v:
    n += 1
print(n)


#정답 코드
a,b,v = map(int, input().split())

if (v-b) % (a-b) == 0:
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b) + 1)