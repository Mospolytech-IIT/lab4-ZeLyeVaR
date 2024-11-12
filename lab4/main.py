from functions import divide, square_root, calculate_average, process_data, risky_calculation, generate_exception

def main():
    try:
        print(divide(10, 2))
        print(square_root(16))
        print(calculate_average([1, 2, 3, 4, 5]))
        process_data([1, 2, 3])
        risky_calculation(-10)
        generate_exception(-5)
    except Exception as e:
        print(f"Произошла ошибка в главной функции: {e}")

if __name__ == "__main__":
    main()
