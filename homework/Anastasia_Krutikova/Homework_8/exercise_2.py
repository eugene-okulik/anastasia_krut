#  Задание_2

def fib(limit=100000000):
    number_1 = 0
    number_2 = 1
    f_count = 0
    while f_count < limit:
        yield number_1
        number_1, number_2 = number_2, number_1 + number_2
        f_count += 1


count = 0

for number in fib(1000000):
    count += 1
    if count == 5:
        print(number)
    elif count == 200:
        print(number)
    elif count == 1000:
        print(number)
    elif count == 100000:
        print(number)
