import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


def multiplucation_numbers(list_of_numbers: list[float]) -> float:
    result = 1.0
    for number in list_of_numbers:
        result *= number
    return result


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
    except ValueError as e:
        ValueError: logging.error("Given elements not numbers")
    else:
        if len(arg_list_numbers) < 2:
            logging.warning("Too less numbers, cannot calculate, result will be a given number")
        if (choice == '2' or choice == '4') and len(arg_list_numbers) > 2:
            logging.warning("Only two first numbers will be taken to action")
        if choice == '2':
            result = arg_list_numbers[0] - arg_list_numbers[1]
            action = "subtraction"
        elif choice == '4':
            action = "division"
            if arg_list_numbers[1] == 0.0:
                logging.error("Cannot division by zero!")
            else:
                result = arg_list_numbers[0] / arg_list_numbers[1]
        elif choice == '1':
            result = sum(arg_list_numbers)
            action = "addition"
        else:
            result = multiplucation_numbers(arg_list_numbers)
            action = "multiplication"
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
                        result = multiplucation_numbers(numbers)
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