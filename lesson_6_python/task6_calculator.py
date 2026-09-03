import operator

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")

def get_operator():
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow,
        '%': operator.mod
    }
    allowed_ops = ', '.join(ops.keys())
    
    while True:
        op = input(f"Выберите оператор ({allowed_ops}): ").strip()
        if op in ops:
            return op, ops[op]
        print(f"Ошибка: доступны только: {allowed_ops}")

def main():
    num1 = get_float("Введите первое число: ")
    num2 = get_float("Введите второе число: ")
    op, func = get_operator()
    if op in ('/', '%') and num2 == 0:
        print("Ошибка: деление на ноль невозможно.")
        return
    
    result = func(num1, num2)
    if result.is_integer():
        print(f"Результат: {num1} {op} {num2} = {int(result)}")
    else:
        print(f"Результат: {num1} {op} {num2} = {result:.2f}")

if __name__ == "__main__":
    main()