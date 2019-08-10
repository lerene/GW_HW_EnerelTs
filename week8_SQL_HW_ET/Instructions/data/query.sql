-- 1. List the following details of each employee: 
-- employee number, last name, first name, gender, and salary.
-- Pick the tables that we need: employee, salary
SELECT * 
FROM emp
LEFT JOIN salaries
ON (emp.emp_no = salaries.emp_no)

SELECT emp.emp_no, emp.last_name, emp.first_name, emp.gender, salaries.salary
FROM emp
LEFT JOIN salaries
ON (emp.emp_no = salaries.emp_no)

-- 2. List employees who were hired in 1986.
SELECT *
FROM emp
WHERE hire_date BETWEEN '01-jan-1986' AND '31-dec-1986';

-- 3. List the manager of each department with the following information: 
-- department number, department name, the manager's employee number, 
-- last name, first name, and start and end employment dates.
SELECT * 
FROM departments, dept_manager, emp
WHERE departments.dept_no = dept_manager.dept_no and dept_manager.emp_no = emp.emp_no

SELECT departments.dept_no, departments.dept_name, dept_manager.emp_no, emp.last_name, emp.first_name, dept_manager.from_date, dept_manager.to_date
FROM emp, dept_manager, departments
WHERE departments.dept_no = dept_manager.dept_no and dept_manager.emp_no = emp.emp_no

-- 4. List the department of each employee with the following information: 
-- employee number, last name, first name, and department name.
SELECT * 
FROM emp, dept_emp, departments
WHERE emp.emp_no = dept_emp.emp_no and emp.emp_no = dept_emp.emp_no and dept_emp.dept_no = departments.dept_no

SELECT emp.emp_no, emp.last_name, emp.first_name, departments.dept_name
FROM emp, dept_emp, departments
WHERE emp.emp_no = dept_emp.emp_no and emp.emp_no = dept_emp.emp_no and dept_emp.dept_no = departments.dept_no


-- 5. List all employees whose first name is "Hercules" and last names begin with "B."
SELECT *
FROM emp
WHERE first_name='Hercules' AND last_name LIKE 'B%';

-- 6. List all employees in the Sales department, including their employee number, 
-- last name, first name, and department name.
SELECT * 
FROM emp, dept_emp, departments
WHERE emp.emp_no = dept_emp.emp_no and emp.emp_no = dept_emp.emp_no and dept_emp.dept_no = departments.dept_no
 
SELECT emp.emp_no, emp.last_name, emp.first_name, departments.dept_name
FROM emp, dept_emp, departments
WHERE emp.emp_no = dept_emp.emp_no and emp.emp_no = dept_emp.emp_no and dept_emp.dept_no = departments.dept_no
AND departments.dept_name = 'Sales'

-- 7. List all employees in the Sales and Development departments, including their 
-- employee number, last name, first name, and department name.

SELECT emp.emp_no, emp.last_name, emp.first_name, departments.dept_name
FROM emp, dept_emp, departments
WHERE emp.emp_no = dept_emp.emp_no AND emp.emp_no = dept_emp.emp_no AND dept_emp.dept_no = departments.dept_no
AND (departments.dept_name = 'Sales' OR departments.dept_name = 'Development')

-- 8. In descending order, list the frequency count of employee last names, 
-- i.e., how many employees share each last name.
SELECT last_name,
COUNT(last_name) AS "frequency"
FROM emp
GROUP BY last_name
ORDER BY
COUNT(last_name) DESC;