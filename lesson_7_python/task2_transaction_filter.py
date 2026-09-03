# Список транзакций от платёжного шлюза
raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10", "SUCCESS:0", "SUCCESS:250", "ERROR:200"]

# в одну строку:
# 1 берём только те, что начинаются с "SUCCESS:"
# 2 разбиваем по ":" и берём вторую часть (сумму)
# 3 превращаем в число int
# 4 оставляем только положительные (> 0)
filtered = [int(t.split(':')[1]) for t in raw_transactions if t.startswith('SUCCESS:') and int(t.split(':')[1]) > 0]

print(f"Очищенные транзакции: {filtered}")