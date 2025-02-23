#  Задание_4

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = PRICE_LIST.splitlines()

products = [x.split()[0] for x in new_list]
price = [int(x.split()[1][:-1]) for x in new_list]

new_dict = dict(zip(products, price))
print(new_dict)
