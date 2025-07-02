"""
Znajdź pierwszych 30 liczb podzielnych bez reszty przez 6 Wykorzystując pętlę while zwróć w konsoli wyłącznie pierwszych 30 liczb, które możemy bez reszty podzielić przez 6.

Wynik widoczny w konsoli powinien zaczynać się następująco:

6 12 18 ...
"""

number = 6
amount = 1
print("Version 1 - while without if")
while amount <= 30:
    print(number, end=" ")
    amount += 1
    number += 6


number = 1
amount = 1
print()
print("Version 2 - while with if")
while amount <= 30:
    if number % 6 == 0:
        print(number, end=" ")
        amount += 1
    number += 1

number = 6
print()
print("Version 3 - for")
for amount in range(1, 31):
    print(number, end=" ")
    number += 6

number = 6
print()
print("Version 4 - for")
for amount in range(1, 31):
    print(number * amount, end=" ")

