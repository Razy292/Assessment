SELECT department_name,
COUNT(IF(gender = 'women', 1, NULL)) as women,
COUNT(IF(gender = 'men', 1, NULL)) as men
FROM department_table
JOIN student_table
ON student_table.department_id = department_table.department_id
GROUP BY department_name