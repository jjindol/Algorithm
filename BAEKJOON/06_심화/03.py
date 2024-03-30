n = int(input())

for i in range(1,n+1):
    print(" " * (n-i), "*" * (2*i-1))

for j in range(2*n-3, 0, -2):
    spaces = (2*n-1-j)//2
    print(" "*spaces, "*"*j)