SELECT department_name, AVG(gpa)
FROM department_table
JOIN student_table
ON student_table.department_id = department_table.department_id
GROUP BY department_name