ABSOLUTE_ZERO_CELSIUS = -273.15

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число (например, 25.5).")

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def main():
    celsius = get_float("Введите температуру в градусах Цельсия: ")
    
    if celsius < ABSOLUTE_ZERO_CELSIUS:
        print("Ошибка: температура ниже абсолютного нуля (-273.15°C)!")
        return
    
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:.2f}°C это {fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()