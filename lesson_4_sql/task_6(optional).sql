-- Найти ProjectName всех проектов, в которых 'Bob Johnson' работал более 150 часов.
SELECT p.ProjectName
FROM Projects p
JOIN EmployeeProjects ep ON p.ProjectID = ep.ProjectID
JOIN Employees e ON ep.EmployeeID = e.EmployeeID
WHERE e.FirstName = 'Bob' AND e.LastName = 'Johnson'
  AND ep.HoursWorked > 150;

-- Увеличить Budget всех проектов на 10%, если к ним назначен хотя бы один сотрудник из отдела 'IT'.
UPDATE Projects
SET Budget = Budget * 1.10
WHERE ProjectID IN (
    SELECT DISTINCT ep.ProjectID
    FROM EmployeeProjects ep
    JOIN Employees e ON ep.EmployeeID = e.EmployeeID
    WHERE e.Department = 'IT'
);

-- Для любого проекта, у которого еще нет EndDate (EndDate IS NULL),
-- установить EndDate на один год позже его StartDate.
UPDATE Projects
SET EndDate = StartDate + INTERVAL '1 year'
WHERE EndDate IS NULL;

-- Вставить нового сотрудника и немедленно назначить его на проект 'Website Redesign' с 80 отработанными часами,
-- все в рамках одной транзакции. Использовать предложение RETURNING, чтобы получить EmployeeID.
BEGIN; -- начало транзакции
-- вставляем нового сотрудника и сохраняем его ID
WITH new_employee AS (
    INSERT INTO Employees (FirstName, LastName, Department, Salary)
    VALUES ('Alex', 'Kozlov', 'IT', 70000.00)
    RETURNING EmployeeID
)
-- Назначаем его на проект 'Website Redesign' (ProjectID получаем динамически)
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT 
    ne.EmployeeID,
    (SELECT ProjectID FROM Projects WHERE ProjectName = 'Website Redesign'),
    80
FROM new_employee ne;

COMMIT; -- фиксируем транзакцию

SELECT * FROM Employees ORDER BY EmployeeID DESC LIMIT 1;
SELECT * FROM EmployeeProjects WHERE EmployeeID = (SELECT MAX(EmployeeID) FROM Employees);