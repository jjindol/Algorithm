#조건문 형태만 만들어 놓고 처리하는 부분은 비워놓을 때
a = 85

if a >= 80:
    pass
else:
    print('a < 80')


b = [1,2,3,4,5,5]
c = map(str, b) #형 변환
if '1' in c:
    print(True)
else:
    print(False)