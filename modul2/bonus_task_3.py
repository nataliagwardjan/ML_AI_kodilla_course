"""
Kod do przekopiowania:

num = 30
fibonacci = []
Stwórz listę zawierającą kolejne elementy ciągu Fibonacciego

Ciąg Fibonacciego to sekwencja, w której każda kolejna liczba jest sumą dwóch poprzednich liczb.

Na przykład:

1,1,2,3,5,8,13... Napisz program, który zwraca listę kolejnych 30 elementów ciągu Fibonacciego.

Listę zawierającą kolejne elementy ciągu przypisz do zmiennej fibonacci
"""

num = 30
fibonacci = []

while len(fibonacci) <= num:
    if len(fibonacci) == 0 or len(fibonacci) == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(sum(fibonacci[-2:]))

print(f"Fibonacci: {fibonacci}")