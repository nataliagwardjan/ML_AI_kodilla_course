"""
Zadanie 1
Użyj listy składanej, aby stworzyć listę sześcianów (potęgi trzeciej) liczb z zakresu od 1 do
10. Następnie użyj pętli for in, aby zwrócić w konsoli liczby niepodzielne przez 2.

Zadanie 2
Dana jest lista: [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]. Zadeklaruj ją w
Pythonie, a następnie użyj slicingu, by otrzymać listę, która zawiera tylko zera z tej kolekcji.
Potem użyj tej samej techniki do zwrócenia listy, która zawiera wszystkie inne liczby tylko
nie zera z tej kolekcji.
Możesz wykonać to w kilku krokach (stworzenie kilku list pośrednich), jak i w jednym.
"""

# Task 1

list_of_cubes = [number ** 3 for number in range(1, 11)]

print("Task 1")
print(f"List of all numbers: {list_of_cubes}")
print("Odd numbers: ")
for number in list_of_cubes:
    if number % 2 != 0:
        print(number, end=' ')

# Task 2
print()
print(10 * '-')
print("Task 2")

list_of_numbers = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]

list_of_zeros = [number for number in list_of_numbers if number == 0]
list_of_not_zeros = [number for number in list_of_numbers if number != 0]

print("As list comprehension")
print(f"Given list: {list_of_numbers}")
print(f"Zeros list: {list_of_zeros}")
print(f"Not zero list: {list_of_not_zeros}")

list_of_zeros_1 = list_of_numbers[1:4]
list_of_zeros_2 = list_of_numbers[5:10]
list_of_zeros_3 = list_of_numbers[-2:]
list_of_zeros = list_of_zeros_1 + list_of_zeros_2 + list_of_zeros_3

list_of_not_zero1 = list_of_numbers[0]
list_of_not_zero2 = list_of_numbers[4]
list_of_not_zero3 = list_of_numbers[-4:-2]
list_of_not_zeros = [list_of_not_zero1, list_of_not_zero2] + list_of_not_zero3

print("As slicing")
print(f"Given list: {list_of_numbers}")
print(f"Zeros list: {list_of_zeros}")
print(f"Not zero list: {list_of_not_zeros}")
