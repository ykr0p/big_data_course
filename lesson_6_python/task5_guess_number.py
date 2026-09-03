import random

def get_integer_in_range(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            print(f"Число должно быть от {low} до {high}.")
        except ValueError:
            print("Ошибка: введите целое число.")

def get_hint(guess, secret):
    diff = guess - secret

    if diff > 0:
        if diff >= 10:
            return "Слишком много!"
        elif diff >= 5:
            return "Много!"
        else:
            return "Немного меньше!"
    else:
        abs_diff = -diff
        if abs_diff >= 10:
            return "Слишком мало!"
        elif abs_diff >= 5:
            return "Мало!"
        else:
            return "Немного больше!"

def main():
    secret = random.randint(1, 20)
    attempts = 5

    print(f"Я загадал число от 1 до 20. У тебя {attempts} попыток!")

    while attempts > 0:
        guess = get_integer_in_range("Введите число: ", 1, 20)

        if guess == secret:
            print("Красафчик, ты угадал!")
            break

        print(get_hint(guess, secret))

        attempts -= 1
        if attempts > 0:
            print(f"Осталось попыток: {attempts}")
        else:
            print(f"Игра окончена. Загаданное число было: {secret}")

if __name__ == "__main__":
    main()