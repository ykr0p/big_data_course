# Данные телеметрии: имя_сервера, загрузка_CPU, RAM, статус
system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online")
]

# списки для активных серверов, их CPU и RAM
active_servers = []
cpu_loads = []
ram_usages = []

# проходим по каждому серверу, распаковывая кортеж в переменные
for node_name, cpu_load, ram_usage, status in system_telemetry:
    if status == "online":          # берём только работающие серверы
        active_servers.append(node_name)
        cpu_loads.append(cpu_load)
        ram_usages.append(ram_usage)

# количество активных серверов
active_count = len(active_servers)

# средняя загрузка CPU (округляем до 2 знаков)
avg_cpu = round(sum(cpu_loads) / active_count, 2) if active_count > 0 else 0

# максимальное использование RAM
max_ram = max(ram_usages) if ram_usages else 0

# собираем итоговый отчёт в словарь
result = {
    "active_nodes_count": active_count,
    "metrics": {
        "average_cpu": avg_cpu,
        "max_ram": max_ram
    }
}

print(f"Активные узлы в сети: {active_servers}")
print("Итоговый отчет телеметрии:")
print(result)