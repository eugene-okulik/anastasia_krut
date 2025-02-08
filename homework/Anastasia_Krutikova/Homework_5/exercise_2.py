#  Задание 2

result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'

# result_1_new = int(result_1.split()[2]) + 10
# print(result_1_new)

index_result_1 = (result_1.index('42'))
sum_result_1 = int((result_1[index_result_1:])) + 10
print(sum_result_1)

index_result_2 = (result_2.index('514'))
sum_result_2 = int((result_2[index_result_2:])) + 10
print(sum_result_2)

index_result_3 = (result_3.index('9'))
sum_result_3 = int((result_3[index_result_3:])) + 10
print(sum_result_3)
