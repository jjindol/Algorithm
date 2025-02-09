n, m = map(int, input().split())

arr1 = {input().strip() for _ in range(n)}
arr2 = {input().strip() for _ in range(m)}

# 교집합을 사용하여 빠르게 공통 요소 찾기
result = sorted(arr1 & arr2)

print(len(result))
print("\n".join(result))