# Исходная необработанная строка из источника данных
raw_user_record = " 10827 ; aLexAnDer_vLaDimiRov ; mInSk ; ACTIVE "

# разбиваем строку по точке с запятой -> получаем список из 4 элементов
parts = raw_user_record.split(';')

# убираем пробелы слева и справа у каждого элемента
user_id = parts[0].strip()
username = parts[1].strip()
city = parts[2].strip()
status = parts[3].strip()

# добавляем префикс UID- к ID
user_id = f"UID-{user_id}"

# в имени заменяем _ на пробел, затем каждое слово с большой буквы
username = username.replace('_', ' ').title()

# город -> все буквы заглавные
city = city.upper()

# статус -> все буквы маленькие
status = status.lower()

# склеиваем все части через разделитель " | "
result = ' | '.join([user_id, username, city, status])

print(f"Нормализованная запись: {result}")