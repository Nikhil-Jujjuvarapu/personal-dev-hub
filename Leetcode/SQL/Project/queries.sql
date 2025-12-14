SELECT *
FROM (
  SELECT
    d.dept_name,
    e.first_name || ' ' || e.last_name AS emp_name,
    s.salary,
    DENSE_RANK() OVER (PARTITION BY d.dept_name ORDER BY s.salary DESC) AS rnk
  FROM prja.employees e
  JOIN prja.emp_salary s ON e.emp_id = s.emp_id
  JOIN prja.departments d ON e.dept_id = d.dept_id
) t
WHERE rnk <= 2
ORDER BY dept_name, rnk, salary DESC;

SELECT
  e.first_name || ' ' || e.last_name AS emp_name,
  d.dept_name,
  s.salary,
  ROUND(AVG(s.salary) OVER (PARTITION BY d.dept_name), 2) AS dept_avg,
  s.salary - AVG(s.salary) OVER (PARTITION BY d.dept_name) AS sal_diff
FROM prja.employees e
JOIN prja.emp_salary s ON e.emp_id = s.emp_id
JOIN prja.departments d ON e.dept_id = d.dept_id
ORDER BY d.dept_name, sal_diff DESC;

SELECT
  d.dept_name,
  e.first_name || ' ' || e.last_name AS emp_name,
  s.salary,
  SUM(s.salary) OVER (
    PARTITION BY d.dept_name
    ORDER BY s.salary DESC
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS running_total
FROM prja.employees e
JOIN prja.emp_salary s ON e.emp_id = s.emp_id
JOIN prja.departments d ON e.dept_id = d.dept_id
ORDER BY d.dept_name, running_total DESC;

SELECT
  d.dept_name,
  e.first_name || ' ' || e.last_name AS emp_name,
  s.salary,
  LAG(s.salary) OVER (PARTITION BY d.dept_name ORDER BY s.salary DESC) AS prev_emp_sal,
  s.salary - LAG(s.salary) OVER (PARTITION BY d.dept_name ORDER BY s.salary DESC) AS sal_diff
FROM prja.employees e
JOIN prja.emp_salary s ON e.emp_id = s.emp_id
JOIN prja.departments d ON e.dept_id = d.dept_id
ORDER BY d.dept_name, s.salary DESC;

WITH dept_stats AS (
  SELECT
    d.dept_id,
    d.dept_name,
    COUNT(e.emp_id)        AS total_employees,
    ROUND(AVG(s.salary), 2) AS avg_salary,
    SUM(s.salary)          AS total_salary
  FROM prja.departments d
  LEFT JOIN prja.employees e ON e.dept_id = d.dept_id
  LEFT JOIN prja.emp_salary s ON s.emp_id = e.emp_id
  GROUP BY d.dept_id, d.dept_name
)
SELECT
  dept_name,
  total_employees,
  avg_salary,
  total_salary,
  DENSE_RANK() OVER (ORDER BY total_salary DESC) AS dept_rank_by_total_salary
FROM dept_stats
ORDER BY dept_rank_by_total_salary;


SELECT *
FROM (
  SELECT
    e.first_name || ' ' || e.last_name AS emp_name,
    d.dept_name,
    s.salary,
    RANK() OVER (ORDER BY s.salary DESC) AS rnk
  FROM prja.employees e
  JOIN prja.emp_salary s ON e.emp_id = s.emp_id
  JOIN prja.departments d ON e.dept_id = d.dept_id
) t
WHERE rnk <= 5
ORDER BY rnk, salary DESC;


SELECT
  e.first_name || ' ' || e.last_name AS emp_name,
  d.dept_name,
  s.salary,
  CASE
    WHEN s.salary > 100000 THEN 'High'
    WHEN s.salary >= 70000 AND s.salary <= 100000 THEN 'Medium'
    ELSE 'Low'
  END AS salary_band
FROM prja.employees e
JOIN prja.emp_salary s ON e.emp_id = s.emp_id
JOIN prja.departments d ON e.dept_id = d.dept_id
ORDER BY salary DESC;


WITH emp_years AS (
  SELECT
    e.emp_id,
    e.first_name || ' ' || e.last_name AS emp_name,
    e.joined_on AS doj,
    s.salary,
    -- years as decimal: full years + months/12
    EXTRACT(YEAR FROM age(current_date, e.joined_on)) +
    EXTRACT(MONTH FROM age(current_date, e.joined_on)) / 12.0 AS years_exp
  FROM prja.employees e
  JOIN prja.emp_salary s ON e.emp_id = s.emp_id
)
SELECT
  emp_id,
  emp_name,
  doj,
  ROUND(years_exp::numeric, 2) AS years_exp,
  salary,
  CASE
    WHEN years_exp >= 5 THEN ROUND(salary * 0.10, 2)
    WHEN years_exp >= 2 THEN ROUND(salary * 0.05, 2)
    ELSE ROUND(salary * 0.02, 2)
  END AS bonus_amount,
  CASE
    WHEN years_exp >= 5 THEN '10%'
    WHEN years_exp >= 2 THEN '5%'
    ELSE '2%'
  END AS bonus_pct
FROM emp_years
ORDER BY years_exp DESC;


SELECT
  d.dept_name,
  COUNT(*) AS cnt_high_earners
FROM prja.departments d
JOIN prja.employees e ON e.dept_id = d.dept_id
JOIN prja.emp_salary s ON s.emp_id = e.emp_id
WHERE s.salary > 80000
GROUP BY d.dept_name
ORDER BY cnt_high_earners DESC
LIMIT 1;


