#집합의 특징: 중복을 허용하지 않고, 순서가 없다(인덱싱x)

#초기화
data = set([1,1,2,3,4,4,5])
print(data)

data = {1,1,2,3,4,4,5}
print(data)

a = set([1,2,3,4,5])
b = set([1,2,3,8,9])

print(a|b) #합집합
print(a&b) #교집합
print(a-b) #차집합

#관련 함수
data = set([1,2,3])
print(data)

data.add(4) #원소 추가
data.update([5,6]) #원소 여러개 추가
data.remove(3) #원소 삭제

print(data)