#종료 조건
def recursive_function(i):
    #100번 째 출력했을 때 종료되도록 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수 호출')
    recursive_function(i+1)
    print(i, '번째 재귀 함수 종료')

recursive_function(1)