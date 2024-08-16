def add1(a,b):
    return a+b
print(add1(3,7))

def add2(a,b):
    print(a+b)
add2(3,7)

def add3(a,b):
    print(a+b)
add3(b=3, a=7)

#global 키워드의 사용: 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조한다.
a = 0

def func():
    global a
    a+= 1

for i in range(10):
    func()

print(a)

#Lambda
print((lambda a,b: a+b)(3,7))