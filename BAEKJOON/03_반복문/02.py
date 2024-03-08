t = int(input())

sum = []

for _ in range(t):
    a, b = map(int, input().split())
    sum.append(a+b)
    
for result in sum:
    print(result)