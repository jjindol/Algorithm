import sys
input = sys.stdin.readline

def func1(arr, n):
    return round(sum(arr) / n)

def func2(arr,n):
    return arr[(n-1)//2]

def func3(arr):
    d = dict()

    for x in arr:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    max_freq = max(d.values())
    most_freq = [k for k,v in d.items() if v == max_freq]

    if len(most_freq) >= 2:
        return sorted(most_freq)[1]
    else:
        return most_freq[0]

def func4(arr):
    return max(arr) - min(arr)

n = int(input())
    
lst = []

for i in range(n):
    lst.append(int(input()))

lst.sort()
print(func1(lst,n))
print(func2(lst,n))
print(func3(lst))
print(func4(lst))