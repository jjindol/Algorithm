import math

def solution(nums):
    answer = 0
    lst = []
    N = len(nums)

    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                tmp = nums[i] + nums[j] + nums[k]
                lst.append(tmp)

    for i in range(len(lst)):
        if isPrime(lst[i]):
            answer += 1

    return answer


def isPrime(x):
    if x <= 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True