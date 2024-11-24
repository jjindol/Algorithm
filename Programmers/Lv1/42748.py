def solution(array, commands):
    lst = []
    answer = []

    for i in range(len(commands)):
        lst.append(array[commands[i][0] - 1:commands[i][1]])

    for i in range(len(lst)):
        lst[i].sort()

    for i in range(len(lst)):
        answer.append(lst[i][commands[i][2] - 1])

    return answer