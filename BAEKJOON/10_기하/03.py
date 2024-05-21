#풀이1
lst = []
for _ in range(3):
    x,y = map(int, input().split())
    lst.append((x,y))

X = [x for (x,y) in lst]
Y = [y for (x,y) in lst]

result_x = min(X, key=X.count)
result_y = min(Y, key=Y.count)

print(result_x,result_y)


#풀이2
lst1=[]
lst2=[]

for _ in range(3):
    x,y = map(int, input().split())
    lst1.append(x)
    lst2.append(y)

for i in range(3):
    if lst1.count(lst1[i]) == 1:
        X = lst1[i]
    if lst2.count(lst2[i]) == 1:
        Y = lst2[i]
print(X,Y)