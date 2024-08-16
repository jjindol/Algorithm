n = int(input())
lst = []

for i in range(n):
    x = int(input())
    lst.append(x)

lst.sort()
avr = round(sum(lst)/n)
mid = lst[(n-1)//2]

ran = max(lst) - min(lst)

print(avr)
print(mid)

print(ran)