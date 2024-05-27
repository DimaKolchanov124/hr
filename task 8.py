#8.1
sum_ = 0
input_number = int(input('введите число: '))
while input_number != 0:
    sum_ += input_number
    input_number = int(input('введите число: '))
print('ответ: ', sum_)

#8.2
car = {'bmw': {'year': '2017', 'price': 4300000},
     'Mercedes-Benz': {'year': '2017', 'price': 8500000},
     'Alfa Romeo': {'year': '2017', 'price': 2780000}
     }
for value in car.keys():
    print(value)


credit = {'тинкофф': {'view': 'потребительский', 'sum': 1000000, 'interest rate': 6},
    'сбербанк': {'view': 'потребительский', 'sum': 500000, 'interest rate': 8},
    'втб': {'view': 'потребительский', 'sum': 1200000, 'interest rate': 9}
         }
for value in credit.items():
    print(value)



tur = {'турция': {'столица': 'анкара','days': 12, 'price': 100000},
     'италия': {'столица': 'рим','days': 14, 'price': 250000},
     'вьетнам': {'столица': 'Ханой','days': 10, 'price': 18000}
     }
for index, value in tur.items():
    print(index, value)


for i in range(0, 10):
    for j in range(0, 11):
        print(j, end=" ")
    print(i)