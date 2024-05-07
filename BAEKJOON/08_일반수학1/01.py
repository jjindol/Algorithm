'''
n, b = input().split()
print(int(n, int(b)))
'''

n,b = input().split()
n = n[::-1]
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = 0
for i,num in enumerate(n):
    res += (int(b)**i)*(arr.index(num))
print(res)