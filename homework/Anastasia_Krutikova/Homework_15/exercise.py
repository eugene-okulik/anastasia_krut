import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
# cursor.execute('SELECT * FROM students WHERE id = 4761')
# data = cursor.fetchall()
# print(data)

cursor.execute("INSERT INTO students (name, second_name) VALUES ('Thomas', 'Andersen')")
student_id = cursor.lastrowid
# print(student_id)

cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('Matrix_1', {student_id})")
book_id_1 = cursor.lastrowid
# print(book_id_1)

cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('Matrix_2', {student_id})")
book_id_2 = cursor.lastrowid
# print(book_id_2)

cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('Matrix_3', {student_id})")
book_id_3 = cursor.lastrowid
# print(book_id_3)

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('Zion', 1999, 2003)")
group_id = cursor.lastrowid
# print(group_id)

cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")

cursor.execute("INSERT INTO subjets (title) VALUES ('jiu jitsu')")
subject_1 = cursor.lastrowid
# print(subject_1)

cursor.execute("INSERT INTO subjets (title) VALUES ('karate')")
subject_2 = cursor.lastrowid
# print(subject_2)

cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('jiu jitsu lesson_1', {subject_1})")
lesson_jj_1 = cursor.lastrowid
# print(lesson_jj_1)

cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('jiu jitsu lesson_2', {subject_1})")
lesson_jj_2 = cursor.lastrowid
# print(lesson_jj_2)

cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('karate lesson_1', {subject_2})")
lesson_kar_1 = cursor.lastrowid
# print(lesson_kar_1)

cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('karate lesson_2', {subject_2})")
lesson_kar_2 = cursor.lastrowid
# print(lesson_kar_2)

insert_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_marks, [
        (100, lesson_jj_1, student_id),
        (100, lesson_jj_2, student_id),
        (100, lesson_kar_1, student_id),
        (100, lesson_kar_2, student_id)
    ]
)

# cursor.execute(f'SELECT * from marks where student_id = {student_id}')
# print(cursor.fetchall())

cursor.execute(f'SELECT value, student_id FROM marks where student_id = {student_id}')
print(cursor.fetchall())

cursor.execute(f'SELECT title FROM books WHERE taken_by_student_id = {student_id}')
print(cursor.fetchall())

select_query = '''SELECT * 
FROM students s
join `groups`g ON s.group_id = g.id
join books b ON s.id = b.taken_by_student_id
join marks m ON s.id = m.student_id
join lessons l ON m.lesson_id = l.id
join subjets sub ON l.subject_id = sub.id
WHERE s.id = 4761
'''

cursor.execute(select_query)
print(cursor.fetchall())

db.commit()

db.close()
