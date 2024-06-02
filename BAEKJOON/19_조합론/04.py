#풀이1
import math
n, k = map(int, input().split())

result = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
print(result)


#풀이2
def factorial(n):
    tmp = 1

    for i in range(n,0,-1):
        tmp *= i
    return tmp

n, k = map(int, input().split())
result = factorial(n) // (factorial(k)*factorial(n-k))
print(result)