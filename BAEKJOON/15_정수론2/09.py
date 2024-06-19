n = int(input())

i = 1
while(True):
    if i**2 <= n < (i+1)**2:
        print(i)
        break
    i += 1