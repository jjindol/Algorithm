students = []
for i in range(30):
    students.append(i)

for _ in range(28):
    num = int(input())
    students.remove(num)

print(min(students))
print(max(students))