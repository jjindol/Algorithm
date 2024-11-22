def solution(phone_book):
    d = dict()
    for i in range(len(phone_book)):
        d[phone_book[i]] = i

    for phone_number in phone_book:
        tmp = ""
        for number in phone_number:
            tmp += number
            if tmp in d and tmp != phone_number:
                return False

    return True