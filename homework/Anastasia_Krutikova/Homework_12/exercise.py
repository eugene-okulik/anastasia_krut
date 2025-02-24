class Flowers:

    def __init__(self, name, length, color, time_life, fresh, price):
        self.name = name
        self.width = length
        self.color = color
        self.time_life = time_life
        self.fresh = fresh
        self.price = price

    def __repr__(self):
        return f"{self.name}, цвет: {self.color}, цена: {self.price}"


class Rose(Flowers):

    def __init__(self, name, length, color, time_life, fresh, price, spike):
        super().__init__(name, length, color, time_life, fresh, price)
        self.spike = spike


class Tulip(Flowers):

    def __init__(self, name, length, color, time_life, fresh, price, country):
        super().__init__(name, length, color, time_life, fresh, price)
        self.country_of_origin = country


rose = Rose('Роза', 10, 'красный', 3, 2, 1200, True)
tulip = Tulip('Тюльпан', 8, 'жёлтый', 10, 4, 1000, 'Голландия')
gerbera_white = Flowers('Гербера белая', 20, 'белый', 16, 10, 400)
gerbera_yellow = Flowers('Гербера жёлтая', 20, 'жёлтый', 16, 10, 400)
gerbera_green = Flowers('Гербера зелёная', 20, 'зелёный', 16, 10, 400)


class Buket:

    def __init__(self):

        self.flowers_list = []

    def add_flowers(self, flowers):
        self.flowers_list.append(flowers)

    def price_buket(self):
        total_price = sum(flower.price for flower in self.flowers_list)

        return total_price

    def time_life(self):
        common_life_time = sum(flower.time_life for flower in self.flowers_list)
        time_life_buket = round(common_life_time / len(self.flowers_list), 2)

        return time_life_buket

    def sort_buket_price(self):
        return sorted(flower.price for flower in self.flowers_list)

    def sort_buket_fresh(self):
        return sorted(flower.fresh for flower in self.flowers_list)

    def sort_buket_width(self):
        return sorted(flower.width for flower in self.flowers_list)

    def sort_buket_color(self):
        return sorted(flower.color for flower in self.flowers_list)

    def search_color(self, color):
        return [flower.name for flower in self.flowers_list if flower.color == color]


my_buket = Buket()

my_buket.add_flowers(rose)
my_buket.add_flowers(tulip)
my_buket.add_flowers(gerbera_white)
my_buket.add_flowers(gerbera_yellow)
my_buket.add_flowers(gerbera_green)

print(my_buket.flowers_list)

print(my_buket.price_buket())

print(my_buket.time_life())

print(my_buket.sort_buket_price())
print(my_buket.sort_buket_fresh())
print(my_buket.sort_buket_width())
print(my_buket.sort_buket_color())

print(my_buket.search_color('жёлтый'))
