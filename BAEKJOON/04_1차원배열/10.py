n = int(input())
num = []
score = input().split()

for x in score:
    num.append(int(x))

M = max(num)
for i in range(n):
    num[i] = int(score[i]) / M*100
    
print(sum(num)/n)