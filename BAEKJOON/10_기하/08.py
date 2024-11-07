a,b,c = map(int, input().split())

if a < b+c and b < a+c and c < a+b:
    print(a+b+c)
elif a >= b+c:
    a = b+c-1
    print(a+b+c)
elif b >= a+c:
    b = a+c-1
    print(a+b+c)
elif c >= a+b:
    c = a+b-1
    print(a+b+c)