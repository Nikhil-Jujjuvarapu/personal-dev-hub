-- ===============================
-- 1. Departments Table
-- ===============================
CREATE TABLE prja.departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- ===============================
-- 2. Employees Table
-- ===============================
CREATE TABLE prja.employees (
    emp_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(20),
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    dept_id INT REFERENCES prja.departments(dept_id) ON DELETE SET NULL,
    joined_on DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT TRUE
);

-- ===============================
-- 3. Employee Salary Table
-- ===============================
CREATE TABLE prja.emp_salary (
    emp_slr_id SERIAL PRIMARY KEY,
    emp_id INT REFERENCES prja.employees(emp_id) ON DELETE SET NULL,
    dept_id INT REFERENCES prja.departments(dept_id) ON DELETE SET NULL,
    doj DATE,  -- no need to reference employees.joined_on
    salary NUMERIC(10,2) CHECK (salary > 0),
    band INT CHECK (band BETWEEN 1 AND 10),
    years_of_exp INT CHECK (years_of_exp >= 0),
    cmpny_exp INTERVAL GENERATED ALWAYS AS (CURRENT_DATE - doj) STORED
);

-- ===============================
-- 4. Employee Address Table
-- ===============================
CREATE TABLE prja.emp_addr (
    addr_id SERIAL PRIMARY KEY,
    emp_id INT REFERENCES prja.employees(emp_id) ON DELETE SET NULL,
    primary_addr VARCHAR(100) NOT NULL,
    sec_addr VARCHAR(100),
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    ctry VARCHAR(50) DEFAULT 'India',
    postal_code VARCHAR(10)
);
