#  Задание 3

#  Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

#  var_1
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

name_1, name_2, name_3 = students
math, biology, geography = subjects

print(f"Students {name_1}, {name_2}, {name_3} study these subjects: {math}, {biology}, {geography}")

#  var_2
print(f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}")
