import csv

import os

import mysql.connector as mysql
import dotenv

dotenv.load_dotenv()

# print(os.getenv('DB_USER'))

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)

path = os.path.dirname(os.path.dirname(base_path))
# print(path)
file_path = os.path.join(path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    print(file_data)
    for row in file_data:
        data.append(row)


print(data)

query = '''
SELECT s.name, s.second_name, g.title as group_title, b.title as book_title, sub.title as subject_title,
l.title as lesson_title, m.value as mark_value
FROM students s
JOIN `groups`g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets sub ON l.subject_id = sub.id
'''
cursor.execute(query)
result_db = cursor.fetchall()
print(result_db)


def find_mis_values(data_list, db_list):

    missing_values = []
    for entry in data_list:
        if entry not in db_list:
            missing_values.append(entry)
    return missing_values


missing_in_bd = find_mis_values(data, result_db)

if missing_in_bd:
    for missing_val in missing_in_bd:
        print(missing_val)
