import os
import datetime


''' 
1. 2023-11-27 20:34:13.212967 - распечатать эту дату, но на неделю позже. Должно получиться 2023-12-04 20:34:13.212967
2. 2023-07-15 18:25:10.121473 - распечатать какой это будет день недели
3. 2023-06-12 15:23:45.312167 - распечатать сколько дней назад была эта дата

'''


base_path = os.path.dirname(__file__)

eugene_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(eugene_path, 'eugene_okulik', 'hw_13', 'data.txt')
#print(eugene_file_path)


def read_file():
    with open(eugene_file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line.split()[1:3]


for index, date in enumerate(read_file()):
    date_new = (" ".join(date))
    date_new = datetime.datetime.strptime(date_new, '%Y-%m-%d %X.%f')
    # print(type(date_new))
    # print(date_new)
    now = datetime.datetime.now()
    # print(type(now))

    if index == 0:
        date_1 = date_new + datetime.timedelta(days=7)
        print(date_1)

    elif index == 1:
        date_2 = date_new.strftime('%A')
        print(date_2)

    elif index == 2:
        date_3 = now - date_new
        date_3_diff = date_3.days
        print(date_3_diff)
