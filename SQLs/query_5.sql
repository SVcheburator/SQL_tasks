SELECT t.teacher_name, s.subject_name 
FROM teachers t 
JOIN subjects s ON s.teacher_id =  t.id
GROUP BY s.subject_name;