"""
Stwórz pętlę, która wydrukuje w konsoli liczby kolejno od 10 do 1 Oczekiwany wynik w konsoli:

10 9 8 7 6 5 4 3 2 1
"""

print("Using for loop")
for i in range(1, 11):
    print(11 - i, end=" ")

print()
print("Using for loop reverse")
for i in range(10, 0, -1):
    print(i, end=" ")

print()
print("Using while")
number = 10
while number > 0:
    print(number, end=" ")
    number -= 1