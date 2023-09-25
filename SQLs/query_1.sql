SELECT student_id as id, student_name as name, AVG(grade) as avg_grade
FROM grades as g
JOIN students AS s ON s.id = g.student_id
GROUP BY student_id
ORDER BY AVG(grade) DESC
LIMIT 5;