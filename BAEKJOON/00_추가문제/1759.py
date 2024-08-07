from itertools import combinations
import sys
input = sys.stdin.readline

vowels = {'a', 'e', 'i', 'o', 'u'}

def func(L):
    result = []

    # 모든 가능한 조합 생성
    lst = combinations(alphabet, L)

    for x in lst:
        comb_set = set(x)
        vowel_count = len(comb_set & vowels)
        consonant_count = L - vowel_count

        # 조건을 만족하는 조합만 추가
        if vowel_count >= 1 and consonant_count >= 2:
            result.append(''.join(sorted(x)))

    return sorted(result)

L, C = map(int, input().split())
alphabet = input().split()

for word in func(L):
    print(word)