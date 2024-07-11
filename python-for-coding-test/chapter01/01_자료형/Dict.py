data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

key_list = data.keys()
value_list = data.values()

print(key_list)
print(value_list)

#출력 예시1
if 'Apple' in data.values():
    print("Yes")

#출력 예시2
for key in key_list:
    print(data[key])