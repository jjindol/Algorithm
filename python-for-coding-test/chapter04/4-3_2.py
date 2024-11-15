s = input()
row = int(s[1])
column = int(ord(s[0])) - int(ord('a')) + 1

dx = [-2, -2, 2, 2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

def in_range(x,y):
    return 1<=x<=8 and 1<=y<=8

answer = 0
for i in range(8):
    new_row = row + dx[i]
    new_column = column +dy[i]

    if in_range(new_row,new_column):
        answer += 1

print(answer)