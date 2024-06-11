while (True):
    x,y,z = map(int, input().split())
    if x==y==z==0:
        break
    elif x >= y + z or y >= x + z or z >= x + y:
        print("Invalid")
    elif x==y!=z or y==z!=x or x==z!=y:
        print("Isosceles")
    elif x==y==z:
        print("Equilateral")
    elif x!=y!=z:
        print("Scalene")