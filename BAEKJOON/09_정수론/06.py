import sys
input = sys.stdin.readline
n = int(input())
div = 2
lst = []

while n > 1:
    if n % div == 0:
        lst.append(div)
        n //= div
    else:
        div += 1

for num in lst:
    print(num)