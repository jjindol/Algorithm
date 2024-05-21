a, b = map(int, input().split())
A,B = a,b
tmp = a % b

while tmp != 0:
    tmp2 = b % tmp
    b = tmp
    tmp = tmp2

result = A * B // b 
print(result)