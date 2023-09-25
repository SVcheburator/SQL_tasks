SELECT gr.id as group_id, my.subject_name, my.student_name, my.grade
FROM
    (SELECT subject_name, student_id, student_name, grade
	FROM subjects s
	JOIN grades g ON s.id = g.subject_id 
	join students st ON st.id = g.student_id 
	GROUP BY student_id, grade
	ORDER BY grade DESC) as my
JOIN groups gr ON my.student_id = gr.student_id
GROUP BY group_id, my.subject_name, grade;