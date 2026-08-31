import re

def get_name():
    while True:
        raw = input("Как тебя зовут? ").strip()
        if not raw:
            print("Имя не может быть пустым.")
            continue
        if not re.fullmatch(r"[A-Za-zА-Яа-я\s\-']+", raw):
            print("Имя должно содержать только буквы, пробелы, дефисы или апострофы.")
            continue
        formatted = raw.title()
        return formatted

def main():
    name = get_name()
    print(f"Привет, {name}! Приятно познакомиться.")

if __name__ == "__main__":
    main()