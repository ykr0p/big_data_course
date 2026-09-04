# Список ролей из запроса (есть повторы)
requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]

# обязательные админские роли
required_admin_roles = {"admin", "security_officer", "audit_manager"}

# убираем дубликаты - преобразуем список во множество
unique_roles = set(requested_roles)

# какие админские роли уже есть в запросе? (пересечение)
common_roles = unique_roles & required_admin_roles

# каких админских ролей не хватает? (разность)
missing_roles = required_admin_roles - unique_roles

# проверяем, есть ли роль security_officer в запросе
has_security_officer = 'security_officer' in unique_roles

print(f"Уникальные запрошенные роли: {unique_roles}")
print(f"Общие административные роли: {common_roles}")
print(f"Недостающие административные роли: {missing_roles}")
print(f"Наличие роли security_officer в запросе: {has_security_officer}")