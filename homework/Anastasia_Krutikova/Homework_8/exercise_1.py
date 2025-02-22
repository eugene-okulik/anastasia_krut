#  Задание_1

import random


def total_price():
    salary = int(input("Введите цену: "))
    bonus = random.choice([True, False])

    if bonus:
        bonus_random = random.randint(1, 1000)
        price = salary + bonus_random
    else:
        price = salary

    print(f"{salary}, {bonus} - '${price}'")


total_price()
