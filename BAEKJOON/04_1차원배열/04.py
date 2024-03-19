num = []
for i in range(9):
	x = int(input())
	num.append(x)
	
print(max(num))
print(num.index(max(num))+1)