-- Создать функцию PostgreSQL с именем CalculateAnnualBonus,
-- которая принимает employee_id и Salary в качестве входных данных
-- и возвращает рассчитанную сумму бонуса (10 % от Salary) для этого сотрудника.
-- Используйте PL/pgSQL для тела функции.
CREATE OR REPLACE FUNCTION CalculateAnnualBonus(emp_id INT, salary DECIMAL)
RETURNS DECIMAL AS $$
BEGIN
    RETURN salary * 0.10;
END;
$$ LANGUAGE plpgsql;

-- Использовать эту функцию в операторе SELECT, чтобы увидеть потенциальный бонус для каждого сотрудника.
SELECT EmployeeID, FirstName, LastName, Salary,
       CalculateAnnualBonus(EmployeeID, Salary) AS AnnualBonus
FROM Employees;

-- Создать представление (View) с именем IT_Department_View,
-- которое показывает EmployeeID, FirstName, LastName и Salary
-- только для сотрудников из отдела 'IT'.
CREATE OR REPLACE VIEW IT_Department_View AS
SELECT EmployeeID, FirstName, LastName, Salary
FROM Employees
WHERE Department = 'IT';

-- Выбрать данные из вашего представления IT_Department_View.
SELECT * FROM IT_Department_View;