def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число (например, 42).")

def is_even(number):
    return number % 2 == 0

def main():
    number = get_integer("Введите целое число: ")
    if is_even(number):
        print(f"Число {number} – чётное.")
    else:
        print(f"Число {number} – нечётное.")

if __name__ == "__main__":
    main()