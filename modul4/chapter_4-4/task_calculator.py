import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


def addition_numbers(list_of_numbers: list[float]) -> tuple[float, str]:
    result = 0.0
    for number in list_of_numbers:
        result += number
    return result, 'addition'


def subtraction_numbers(list_of_numbers: list[float]) -> tuple[float, str]:
    return (list_of_numbers[0] - list_of_numbers[1]), 'subtraction'


def division_numbers(list_of_numbers: list[float]) -> tuple[float, str] | None:
    if list_of_numbers[1] == 0.0:
        logging.error("Cannot division by zero!")
        return None
    else:
        return (list_of_numbers[0] / list_of_numbers[1]), 'division'


def multiplication_numbers(list_of_numbers: list[float]) -> tuple[float, str]:
    result = 1.0
    for number in list_of_numbers:
        result *= number
    return result, 'multiplication'


calculate_result = {
    '1': addition_numbers,
    '2': subtraction_numbers,
    '3': division_numbers,
    '4': multiplication_numbers
}

print(f"""
Which action do you want to perform? 
Choose: 
1. Addition
2. Subtraction
3. Multiplication
4. Division
""")
choice = input("Your choice: ")
result = None
action = None
if choice != '1' and choice != '2' and choice != '3' and choice != '4':
    logging.warning("Not choose correct option")
else:
    arg = input(
        "Give number and separate it by comma (if you chose addition or multiplication you can give more then two numbers): ")
    arg_list = arg.split(',')
    try:
        arg_list_numbers = [float(item) for item in arg_list]
    except ValueError:
        logging.error("Given elements not numbers")
    else:
        if len(arg_list_numbers) < 2:
            logging.warning("Too less numbers, cannot calculate, result will be a given number")
        if choice in ('2','4') and len(arg_list_numbers) > 2:
            logging.warning("Only two first numbers will be taken to action")
            arg_list_numbers = arg_list_numbers[:2]
        else:
            result, action = calculate_result[choice](arg_list_numbers)
        print(f"You chose {action} for numbers {arg_list_numbers}, result is {result}")

print()
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
