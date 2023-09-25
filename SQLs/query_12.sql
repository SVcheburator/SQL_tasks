SELECT *
FROM 
	(SELECT group_id, student_name, grade as latest_grade, grade_date
	FROM 
		(SELECT s.student_name, grade, grade_date, gr.id as group_id 
		FROM grades g
		JOIN students s ON s.id = g.student_id
		JOIN groups gr ON gr.student_id = g.student_id 
		ORDER BY grade_date DESC) as my
	
	GROUP BY student_name)
ORDER BY group_id;