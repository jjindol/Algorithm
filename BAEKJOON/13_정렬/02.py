lst = []

for _ in range(5):
    x = lst.append(int(input()))

lst.sort()
target_number = lst[2]

print(sum(lst)//5)
print(target_number)