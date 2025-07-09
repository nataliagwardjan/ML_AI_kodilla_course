"""
Zadanie 1
Mamy zadaną listę z imionami: John, Michael, Terry, Eric, Graham. Zamodeluj to
w Pythonie, czyli stwórz listę o nazwie name_list. Zbuduj także słownik
(name_dictionary), w którym dla każdego imienia przypisz liczbę znaków, które na nie
przypadają. Np. „John” to 4 znaki.

Zadanie 2
Masz listę liczb [1, 2, 3, 5, 6, 11, 12, 18, 19, 21].
Stwórz nową listę i ją wydrukuj. Nowa lista powinna zawierać tylko liczby pierwsze z
poprzedniej listy.

Zadanie 3
Oto lista dni tygodnia: ['pon','śro','pią','sob'].

Brakuje tu kilku. Uzupełnij i wydrukuj całość. Ciekawe co będzie trudniejsze – dojście,
których dni brakuje, czy użycie odpowiedniej funkcji.

Zadanie 4
Oto sekwencja kroków do zrobienia herbaty.
• włącz czajnik
• znajdź opakowanie herbaty
• zalej herbatę
• nalej wody do czajnika
• wyjmij kubek
• włóż herbatę do kubka
Kosmita nie wie jak, się robi herbatę... Stwórz sekwencję zgodnie z kolejnością
nieposortowaną. Następnie poprzestawiaj elementy sekwencji tak, żeby kosmita mógł zrobić
sobie herbatę.
"""
import math

# Task 1
name_list = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
name_dict = {}

for name in name_list:
    name_dict[name] = len(name)

print("Task 1")
for key, value in name_dict.items():
    print(f'name = {key}, length = {value}')

# Task 2
print()
print(10 * '-')
print("Task 2")
list_of_numbers = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]

prime_numbers = []

for number in list_of_numbers:
    is_prime = True
    if number == 0 or number == 1:
        is_prime = False
    else:
        for n in range(2, int(math.sqrt(number)) + 1):
            if number % n == 0:
                is_prime = False
    if is_prime:
        prime_numbers.append(number)

print("Version 1")
print(f"Original numbers: {list_of_numbers}")
print(f"Prime numbers: {prime_numbers}")


def is_prime_number(number: int) -> bool:
    if number == 0 or number == 1:
        return False
    for n in range(2, int(math.sqrt(number)) + 1):
        if number % n == 0:
            return False
    return True


prime_numbers = [number for number in list_of_numbers if is_prime_number(number=number)]

print()
print("Version 2")
print(f"Original numbers: {list_of_numbers}")
print(f"Prime numbers: {prime_numbers}")

# Task 3
print()
print(10 * '-')
print("Task 3")

days_of_week = ['pon', 'śro', 'pią', 'sob']

print(f"Before add days: {days_of_week}")

days_of_week.insert(1, 'wto')
days_of_week.insert(3, 'czw')
days_of_week.append('nie')

print(f"After add days: {days_of_week}")

# Task 4
print()
print(10 * '-')
print("Task 4")

list_of_steps = ['włącz czajnik', 'znajdź opakowanie herbaty', 'zalej herbatę', 'nalej wody do czajnika',
                 'wyjmij kubek', 'włóż herbatę do kubka']

index_step_1 = list_of_steps.index('nalej wody do czajnika')
index_step_2 = list_of_steps.index('włącz czajnik')
index_step_3 = list_of_steps.index('wyjmij kubek')
index_step_4 = list_of_steps.index('znajdź opakowanie herbaty')
index_step_5 = list_of_steps.index('włóż herbatę do kubka')
index_step_6 = list_of_steps.index('zalej herbatę')

sorted_list_of_steps = [
    list_of_steps[index_step_1],
    list_of_steps[index_step_2],
    list_of_steps[index_step_3],
    list_of_steps[index_step_4],
    list_of_steps[index_step_5],
    list_of_steps[index_step_6]
]

print(f"Unsorted list of steps: {list_of_steps}")
print(f"Sorted list of steps: {sorted_list_of_steps}")

print(f"Steps to make a tea: ")
for idx, task in enumerate(sorted_list_of_steps):
    print(f"Step {idx + 1}: {task}")