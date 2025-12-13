CREATE MATERIALIZED VIEW prja.mv_department_cost AS
SELECT 
    d.dept_name,
    SUM(s.salary) AS total_salary,
    COUNT(e.emp_id) AS total_employees,
    ROUND(AVG(s.salary), 2) AS avg_salary
FROM prja.departments d
JOIN prja.employees e ON e.dept_id = d.dept_id
JOIN prja.emp_salary s ON s.emp_id = e.emp_id
GROUP BY d.dept_name;

REFRESH MATERIALIZED VIEW prja.mv_department_cost;
