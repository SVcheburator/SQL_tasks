SELECT subject_name, student_name, avg_grade
FROM
    (SELECT subject_name, student_id, AVG(grade) as avg_grade
	FROM subjects s
	JOIN grades g ON s.id = g.subject_id 
	GROUP BY student_id
	ORDER BY avg_grade DESC)
JOIN students st ON st.id = student_id
GROUP BY subject_name;