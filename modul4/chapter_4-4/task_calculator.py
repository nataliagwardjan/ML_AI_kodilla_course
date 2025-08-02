import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


def addition_numbers(number_1: float, number_2: float, *additional_numbers: float) -> tuple[float, str]:
    result = number_1 + number_2
    for number in additional_numbers:
        result += number
    return result, 'addition'


def subtraction_numbers(number_1: float, number_2: float) -> tuple[float, str]:
    return (number_1 - number_2), 'subtraction'


def division_numbers(number_1: float, number_2: float) -> tuple[float, str] | None:
    if number_2 == 0.0:
        logging.error("Cannot division by zero!")
        return None
    else:
        return (number_1 / number_2), 'division'


def multiplication_numbers(number_1: float, number_2: float, *additional_numbers: float) -> tuple[float, str]:
    result = number_1 * number_2
    for number in additional_numbers:
        result *= number
    return result, 'multiplication'


calculate_result = {
    '1': addition_numbers,
    '2': subtraction_numbers,
    '3': division_numbers,
    '4': multiplication_numbers
}


def calculate(your_choice: str):
    result = None
    action = None
    if your_choice not in ('1', '2', '3', '4'):
        logging.warning("Not choose correct option")
    else:
        arg = input(
            "Give number and separate it by comma (if you chose addition or multiplication you can give more then two numbers): ")
        arg_list = arg.split(',')
        try:
            number_1, number_2, *arg_list_numbers = [float(item) for item in arg_list]
        except ValueError:
            logging.error("Given elements not numbers or there is less then 2 numbers")
        else:
            result, action = calculate_result[choice](number_1, number_2, *arg_list_numbers)
    return result, action


if __name__ == '__main__':
    print(f"""
    Which action do you want to perform? 
    Choose: 
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    """)
    choice = input("Your choice: ")
    result, action = calculate(choice)
    print(f"You chose {action}, result is {result}")




"""print()
print("VERSION WITH STRUCTURAL PATTERN MATCHING")
choice = input("Your choice: ")
result = None
action = None

match choice:
    case '1' | '2' | '3' | '4':
        arg = input("Give numbers separated by comma: ")
        arg_list = arg.split(',')

        try:
            numbers = [float(item.strip()) for item in arg_list]
        except ValueError:
            logging.error("Given elements are not valid numbers")
        else:
            if len(numbers) < 2:
                logging.warning("Too few numbers. Returning the only number (or None).")
                result = numbers[0] if numbers else None
            else:
                match choice:
                    case '1':  # Addition
                        result = sum(numbers)
                        action = "addition"
                    case '2':  # Subtraction
                        action = "subtraction"
                        result = numbers[0] - numbers[1]
                        if len(numbers) > 2:
                            logging.warning("Only the first two numbers were used for subtraction.")
                    case '3':  # Multiplication
                        result = multiplication_numbers(numbers)
                        action = "multiplication"
                    case '4':  # Division
                        action = "division"
                        if numbers[1] == 0:
                            logging.error("Cannot divide by zero!")
                            result = None
                        else:
                            result = numbers[0] / numbers[1]
                        if len(numbers) > 2:
                            logging.warning("Only the first two numbers were used for division.")

            print(f"You chose {action} for numbers {numbers}, result is {result}")
    case _:
        logging.warning("Invalid option chosen.")
"""