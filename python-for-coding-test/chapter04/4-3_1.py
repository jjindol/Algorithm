s = input()
row = int(s[1])
column = int(ord(s[0])) - int(ord('a')) + 1

steps = [(-2,1),(-2,-1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

def in_range(x,y):
    return 1<=x<=8 and 1<=y<=8

answer = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if in_range(next_row, next_column):
        answer += 1

print(answer)