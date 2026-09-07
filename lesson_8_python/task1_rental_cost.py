MAX_RENTAL_BATCH_LIMIT = 150.0


def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0) -> tuple[float, bool]:
    final_sum = quantity * rental_rate * (1 - discount)
    final_sum = round(final_sum, 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return final_sum, is_limit_exceeded


def main():
    print("=== ОТЧЁТ ПО ПАРТИЯМ АРЕНДЫ ===\n")
    
    batches = [
        ("Academy Dinosaur", 30, 2.99, 0.0),
        ("Affair Prejudice", 40, 4.99, 0.1),
        ("Agent Truman", 10, 1.99, 0.0),
        ("African Egg", 50, 3.50, 0.2),
    ]
    
    for name, qty, rate, disc in batches:
        total, exceeded = calculate_rental_batch(qty, rate, disc)
        status = "True" if exceeded else "False"
        print(f"Партия {name}: Сумма {total}$. Превышение лимита: {status}")


if __name__ == "__main__":
    main()