CREATE OR REPLACE VIEW prja.vw_active_employee_summary AS
SELECT 
    e.emp_id,
    e.first_name || ' ' || e.last_name AS full_name,
    d.dept_name,
    s.salary,
    e.joined_on,
    (CURRENT_DATE - e.joined_on) / 365 AS years_in_company
FROM prja.employees e
JOIN prja.departments d ON e.dept_id = d.dept_id
JOIN prja.emp_salary s ON e.emp_id = s.emp_id
WHERE e.is_active = TRUE;


CREATE OR REPLACE VIEW prja.vw_dept_expense AS
SELECT 
    d.dept_name,
    COUNT(e.emp_id) AS total_employees,
    SUM(s.salary) AS total_salary,
    ROUND(AVG(s.salary), 2) AS avg_salary
FROM prja.departments d
LEFT JOIN prja.employees e ON e.dept_id = d.dept_id
LEFT JOIN prja.emp_salary s ON s.emp_id = e.emp_id
GROUP BY d.dept_name;
