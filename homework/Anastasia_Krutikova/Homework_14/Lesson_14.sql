INSERT INTO students (name, second_name) VALUES ('Thomas', 'Andersen')
-- id = 4761
INSERT INTO books (title, taken_by_student_id) VALUES ('Matrix_1', 4761)
INSERT INTO books (title, taken_by_student_id) VALUES ('Matrix_2', 4761)
INSERT INTO books (title, taken_by_student_id) VALUES ('Matrix_3', 4761)
-- SELECT * FROM books WHERE taken_by_student_id = 4761
INSERT INTO `groups` (title, start_date, end_date) VALUES ('Zion', 1999, 2003)
-- SELECT * FROM `groups` WHERE title = 'Zion'
-- id = 3070
UPDATE students SET group_id = 3070 WHERE id = 4761
-- SELECT * FROM students WHERE id = 4761
INSERT INTO subjets (title) VALUES ('jiu jitsu')
-- id = 4952
INSERT INTO subjets (title) VALUES ('karate')
-- id = 4953
INSERT INTO lessons (title, subject_id) VALUES ('jiu jitsu lesson_1',4952)
-- id = 8991
INSERT INTO lessons (title, subject_id) VALUES ('jiu jitsu lesson_2',4952)
-- id = 8992
INSERT INTO lessons (title, subject_id) VALUES ('karate lesson_1', 4953)
-- id = 8993
INSERT INTO lessons (title, subject_id) VALUES ('karate lesson_2', 4953)
-- id = 8994
INSERT INTO marks (value, lesson_id, student_id) VALUES (100, 8991, 4761)
INSERT INTO marks (value, lesson_id, student_id) VALUES (100, 8992, 4761)
INSERT INTO marks (value, lesson_id, student_id) VALUES (100, 8993, 4761)
INSERT INTO marks (value, lesson_id, student_id) VALUES (100, 8994, 4761)
-- SELECT * FROM marks WHERE student_id = 4761

SELECT value, student_id FROM marks where student_id = 4761

SELECT title FROM books WHERE taken_by_student_id = 4761

SELECT * 
FROM students s
join `groups`g ON s.group_id = g.id
join books b ON s.id = b.taken_by_student_id
join marks m ON s.id = m.student_id
join lessons l ON m.lesson_id = l.id
join subjets sub ON l.subject_id = sub.id
WHERE s.id = 4761

