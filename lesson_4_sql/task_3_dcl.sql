-- 1. Создаём пользователя hr_user
CREATE ROLE hr_user WITH LOGIN PASSWORD 'secure_password';

-- 2. Даём право SELECT на таблицу Employees
GRANT SELECT ON Employees TO hr_user;

-- (Тесты 1 и 2 выполнялись в новой сессии под hr_user – результаты на скриншотах)

-- 3. Дополнительно даём права INSERT и UPDATE (от администратора)
GRANT INSERT, UPDATE ON Employees TO hr_user;