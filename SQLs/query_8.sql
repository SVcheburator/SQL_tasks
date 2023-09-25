SELECT teacher_name, my.subject_name, AVG(my.avg_grade) as avg_grade
FROM
    (SELECT subject_name, student_id, AVG(grade) as avg_grade, teacher_id
	FROM subjects s
	JOIN grades g ON s.id = g.subject_id 
	GROUP BY student_id) as my
JOIN teachers t ON my.teacher_id = t.id
GROUP BY my.subject_name;