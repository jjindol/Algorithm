while(True):
    x, y = map(int, input().split())
    if x==0 and y==0:
        break
    if (y % x == 0):
        print("factor")
    elif (x % y == 0):
        print("multiple")
    elif (x%y != 0 or y%x!=0):
        print("neither")
    
