from typing import Any, Tuple, Optional

DEFAULT_RETURN_INDEX_BASE = 10.0


def calculate_overdue_fine(movie_title: str, days_overdue: Any, fine_rate: Any) -> Optional[Tuple[float, float]]:
    try:
        numeric_days = float(days_overdue)
        numeric_rate = float(fine_rate)
        
        total_fine = numeric_days * numeric_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days
        
        print(f"Фильм: '{movie_title}' | Итоговый штраф: {total_fine}$ | Индекс: {return_index}")
        return total_fine, return_index
        
    except TypeError as e:
        print(f"[ОШИБКА ТИПА] Некорректные данные для '{movie_title}': {e}")
        return None
    except ValueError as e:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{movie_title}': {e}")
        return None
    except ZeroDivisionError:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{movie_title}': float division by zero")
        return None
    finally:
        print("--- Проверка транзакции возврата завершена ---\n")


def main():
    print("=== ПРОВЕРКА ВОЗВРАТОВ ===\n")
    
    test_data = [
        ("Matrix", 5, 1.5),
        ("Inception", "пять", 2.0),
        ("Avatar", 0, 2.5),
        ("Interstellar", [3], 3.0),
    ]
    
    for title, days, rate in test_data:
        calculate_overdue_fine(title, days, rate)


if __name__ == "__main__":
    main()