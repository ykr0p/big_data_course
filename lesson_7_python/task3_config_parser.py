# Исходная конфигурация
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

# берём host и port из словаря
host = db_config['connection']['host']
port = db_config['connection']['port']

# безопасно извлекаем ssl_mode, если ключей нет - берём значение по умолчанию
ssl_mode = db_config.get('connection', {}).get('ssl_settings', {}).get('ssl_mode', 'verify-full')

# меняем пользователя на admin
db_config['connection']['user'] = 'admin'

# добавляем новый параметр - максимум соединений
db_config['connection']['max_connections'] = 100

# выводим всё в цикле
print(f"SSL Mode: {ssl_mode}")
print("Параметры соединения:")
for key, value in db_config['connection'].items():
    print(f"* {key}: {value}")