# for문
a = range(10)
print(list(a))

b = range(1, 11)
print(list(b))

for i in range(5, 0, -1):
    print(i)
print('------------')
# while문

i=1
while i<=10:
    print(i)
    i+=1
print('------------')
i=1
while True:
    print(i)
    i += 1
    if (i == 10):
        break
print('------------')

for i in range(1, 11):
    if i%2==0:
        continue
    print(i)
# 짝수인 경우는 건너 뛰고 나머지(홀수) 출력    