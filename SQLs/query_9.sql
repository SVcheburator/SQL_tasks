SELECT st.student_name, sb.subject_name
FROM grades g 
JOIN subjects sb ON sb.id = g.subject_id 
JOIN students st ON st.id = g.student_id 
GROUP BY st.student_name, sb.subject_name;