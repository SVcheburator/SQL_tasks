SELECT gr.id, st.student_name
FROM groups gr
JOIN students st ON st.id = gr.student_id
GROUP BY st.student_name
ORDER BY gr.id;