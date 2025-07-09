"""
Kolejny kod do przekopiowania do nowego pliku:

a = 1
b = -2
c = -5

def equation(a,b,c):
  pass
Zadanie: Program do rozwiązywania równania kwadratowego Stwórz funkcję equation, która jako argumenty bierze zmienne a, b, c będące współczynnikami równania kwadratowego, a następnie oblicza rozwiązania tegoż równania.

Podpowiedź W pierwszej kolejności, funkcja main na podstawie zadanych argumentów powinna obliczać wyróżnik równania kwadratowego - czyli znaną wszystkim ze szkoły średniej deltę.

Następnie w zależności od tego, czy delta jest większa, równa lub mniejsza od 0 - funkcja powinna zwracać odpowiednio:

Jeśli delta > 0: dwa rozwiązania x1 oraz x2. Niech funkcja zwraca je jako krotkę.

Jeśli delta = 0: jedno rozwiązanie x0. Niech funkcja zwraca wtedy tylko tę zmienną.

Jeśli delta < 0: brak rozwiązań. Niech funkcja zwraca wtedy tekst "Brak rozwiązań".
"""
import math

a = 1
b = -2
c = -5


def equation(a, b, c):
    if a != 0:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            print("Brak rozwiązań rzeczywistych")
        elif delta == 0:
            result = -b / (2 * a)
            print(f"Jedno rozwiązanie x = {result}")
        else:
            result_1 = (-b - math.sqrt(delta)) / (2 * a)
            result_2 = (-b + math.sqrt(delta)) / (2 * a)
            print(f"Dwa rozwiązania x1 = {result_1}, x2 = {result_2}")

print("Results")
print(f"For a = {a}, b = {b}, c = {c}")
equation(a, b, c)