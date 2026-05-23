"""Sum a list of integer values provided by the user."""

MAX_ELEMENTS = 100


def prompt_int(message, min_value=None, max_value=None):
    while True:
        value = input(message).strip()
        if not value:
            print("Input cannot be empty. Please enter a valid integer.")
            continue

        try:
            number = int(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if min_value is not None and number < min_value:
            print(f"Please enter a number greater than or equal to {min_value}.")
            continue

        if max_value is not None and number > max_value:
            print(f"Please enter a number less than or equal to {max_value}.")
            continue

        return number


def calculate_sum(numbers):
    return sum(numbers)


def collect_numbers(count):
    numbers = []
    print(f"Enter {count} integer{'s' if count != 1 else ''}:")
    for index in range(1, count + 1):
        numbers.append(prompt_int(f"  {index}: "))
    return numbers


def main():
    try:
        number_of_elements = prompt_int(
            f"Enter the number of elements (1-{MAX_ELEMENTS}): ",
            min_value=1,
            max_value=MAX_ELEMENTS,
        )

        values = collect_numbers(number_of_elements)
        total = calculate_sum(values)

        print(f"Sum of the numbers: {total}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")


if __name__ == "__main__":
    main()
