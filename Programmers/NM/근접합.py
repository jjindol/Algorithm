n,s = map(int, input().split())
arr = list(map(int, input().split()))

def func(arr):
    result = []
    n = len(arr)

    for i in range(n):
        for j in range(i+1,n):
            lst = []
            for k in range(n):
                if k!=i and k!=j:
                    lst.append(arr[k])
            result.append(sum(lst))

    return result

ans = 100
for x in func(arr):
    tmp = abs(x-s)
    ans = min(ans, tmp)
print(ans)