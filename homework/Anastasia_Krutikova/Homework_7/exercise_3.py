# Задание_3

def result_example(number_outside):
    index_result = (number_outside.index(': '))
    sum_result = int((number_outside[index_result + 1:])) + 10
    return sum_result

print(result_example('результат операции: 42'))
print(result_example('результат операции: 54'))
print(result_example('результат работы программы: 209'))
print(result_example('результат: 2'))
