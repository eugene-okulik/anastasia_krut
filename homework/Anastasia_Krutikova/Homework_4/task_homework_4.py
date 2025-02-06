my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [6, 7, 8, 9, 10],
    'dict': {'num_1': 1, 'num_2': 2, 'num_3': 3, 'num_4': 4, 'num_5': 5},
    'set': {1, "one", 2, 4, 5}
}

print("Вывод последнего элемента ключа tuple: ", my_dict['tuple'][-1])

my_dict['list'].append(22)
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = True
my_dict['dict'].pop('num_1')

my_dict['set'].add('new')
my_dict['set'].remove(1)

print(my_dict)
