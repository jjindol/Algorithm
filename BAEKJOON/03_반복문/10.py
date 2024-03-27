N = int(input())

for i in range(N):
    print(" "*(N-i-1) + "*"*(i+1))

# + 연산자는 공백과 별을 하나의 문자열로 연결하여 출력
# , 는 print 함수에 전달되는 인자 구분