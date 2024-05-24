#№1
str_="строка с цифрой 1"
is_substr = "строка" in str_
print('в строке есть слово Строка?', is_substr)
#№2
number = int(input())
conditional_1 = number % 2 == 0
conditional_2 = number % 3 == 0
if conditional_1 and conditional_2:
    print('число кратно 2 и 3')
else:
    print('число не кратно 2 и 3')
#№3
mount = int(input())
bad_condition = \
mount == 12 or \
mount == 1 or \
mount == 2
good_condition = mount in [ 12, 1, 2]
if good_condition:
    print("зима")
else:
    print('не зима')
#№4
hour = int(input())
bad_condition = (6 <= hour) and (hour < 12)
good_condition = 6 <= hour < 12
if good_condition:
    print('утро')
else:
    print('не утро')
#№5
list_ = [5, 6, 7, 8, 9]
result = (4 in list_) and (8 in list_)
print(result)

