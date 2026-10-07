SELECT department_name, COUNT(*)
FROM department_table
JOIN student_table
ON student_table.department_id = department_table.department_id
WHERE gpa > 3.0
GROUP BY department_name