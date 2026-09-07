import time
from typing import Callable, Any, List, Dict, Union

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8


def performance_logger(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = round(time.perf_counter() - start_time, TIME_DECIMALS)
        print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за {elapsed_time} сек.")
        return result
    return wrapper


@performance_logger
def get_sorted_report(data: List[Dict[str, Union[str, float]]]) -> List[Dict[str, Union[str, float]]]:
    return sorted(data, key=lambda item: item['total_sales'], reverse=True)


def main():
    print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===\n")
    
    test_sets = [
        [
            {"category": "Action", "total_sales": 4311.85},
            {"category": "Animation", "total_sales": 4656.30},
            {"category": "Children", "total_sales": 3655.55}
        ],
        [
            {"category": "Classics", "total_sales": 1200.10},
            {"category": "Comedy", "total_sales": 4000.00},
            {"category": "Documentary", "total_sales": 4000.00}
        ],
        [
            {"category": "Drama", "total_sales": 500.00}
        ]
    ]
    
    for idx, test_data in enumerate(test_sets, start=1):
        print(f"--- ТЕСТ {idx} ---")
        sorted_data = get_sorted_report(test_data)
        print("Топ категорий по выручке:")
        for pos, item in enumerate(sorted_data, start=1):
            print(f"{pos}. {item['category']}: {item['total_sales']}")
        print()


if __name__ == "__main__":
    main()