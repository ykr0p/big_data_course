-- Увеличить Salary всех сотрудников в отделе 'HR' на 10%.
UPDATE Employees 
SET Salary = Salary * 1.10 
WHERE Department = 'HR';

-- Обновить Department любого сотрудника с Salary выше 70000.00 на 'Senior IT'.
UPDATE Employees 
SET Department = 'Senior IT' 
WHERE Salary > 70000;

-- Удалить всех сотрудников, которые не назначены ни на один проект в таблице EmployeeProjects.
DELETE FROM Employees 
WHERE EmployeeID NOT IN (
    SELECT DISTINCT EmployeeID FROM EmployeeProjects
);

-- В рамках одной транзакции, вставить новый проект и назначить на него двух существующих 
-- сотрудников с определенным количеством HoursWorked в EmployeeProjects.
BEGIN;
  
   
    INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate)
    VALUES ('New Feature Development', 120000.00, '2024-01-01', '2024-06-30')
    RETURNING ProjectID; 
  
    INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
    VALUES 
        (1, 4, 100),
        (2, 4, 120);

COMMIT;