import datetime


my_data = 'Jan 15, 2023 - 12:05:33'

python_date = datetime.datetime.strptime(my_data, '%b %d, %Y - %X' )
# print(python_date)
# 15.01.2023, 12:05
print((python_date.strftime('%B %d, %Y - %X')).split()[0])

our_data = datetime.datetime.strftime(python_date, '%d.%m.%Y, %H:%M')
print(our_data)
