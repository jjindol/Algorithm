n = int(input())
score = []

result = 0
for i in range(n):
    score.append(int(input()))
    
lst = score[:]

for i in range(n-1,0,-1):
    if score[i]<=score[i-1]:
        score[i-1] = score[i]-1
        
for i in range(n):
    result += lst[i]-score[i]
    
print(result)