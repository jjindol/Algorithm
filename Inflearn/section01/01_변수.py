# 값 교환
a,b = 1,2
a,b = b,a 
print(a,b)

a,b,c = 1,2,3
print(a,b,c)
print(a,b,c, sep='') # 변수 사이 여백x 
print(a,b,c, sep='\n') # 줄 바꿈

print(a, end=' ') # 줄 바꿈x
print(b, end=' ')
print(c)
