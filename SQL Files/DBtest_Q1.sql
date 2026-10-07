SELECT student_name, gpa, department_name
FROM student_table
JOIN department_table
ON student_table.department_id = department_table.department_id
ORDER BY department_name ASC, gpa ASC