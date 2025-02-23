#  Задание_3

def our_decoration(func):

    def wrapper(first, second):
        operator = None

        if first == second:
            operator = '+'
        elif first > second:
            operator = '-'
        elif second > first:
            operator = '/'
        elif first < 0 or second < 0:
            operator = '*'

        return func(first, second, operator)

    return wrapper


@our_decoration
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


a, b = map(int, input("Введите 2 числа: ").split())
result = calc(a, b)
print(result)
