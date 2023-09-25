SELECT gr.id as group_id, my.subject_name, AVG(my.avg_grade) as group_avg_grade
FROM
    (SELECT subject_name, student_id, AVG(grade) as avg_grade
	FROM subjects s
	JOIN grades g ON s.id = g.subject_id 
	GROUP BY student_id
	ORDER BY avg_grade DESC) as my
JOIN groups gr ON my.student_id = gr.student_id
GROUP BY group_id, my.subject_name;