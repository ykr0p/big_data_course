MAX_LIMIT = 1e12

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Значение должно быть положительным (> 0).")
            elif value > MAX_LIMIT:
                print(f"Значение слишком большое (макс. {MAX_LIMIT}).")
            else:
                return value
        except ValueError:
            print("Ошибка: введите число (например, 10.5).")

def main():
    length = get_positive_float("Введите длину прямоугольника: ")
    width = get_positive_float("Введите ширину прямоугольника: ")
    area = length * width
    print(f"Площадь прямоугольника: {area:.2f}")

if __name__ == "__main__":
    main()