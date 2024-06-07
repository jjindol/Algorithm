#재귀 함수
def Fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        value = Fibonacci(n-1)+Fibonacci(n-2)
        return value
    
n = int(input())
print(Fibonacci(n))


#반복문
lst = [0,1]
n = int(input())

for i in range(n-1):
    lst.append(lst[i] + lst[i+1])
print(lst[n])