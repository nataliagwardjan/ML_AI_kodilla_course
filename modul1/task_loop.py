"""
Czas na akcję z Twojej strony. Mając wiedzę o liczbach, operacjach i pętlach przekonaj się, czy potrafisz wykonać następujące zadanie:

Z zakresu liczb od 1 do 100 wypisz wszystkie, które są podzielne przez 3.

Spróbuj zrobić to na dwa sposoby. Użyj pętli for, jak i pętli while. Pisząc pętlę while, wykorzystaj polecenie break.

Jeśli chodzi o zadanie, podejdź do niego systemowo. Najpierw zastanów się nad tym, jak zadeklarować pętlę. Jakiej kolekcji potrzebujesz? Przed pisaniem właściwego ciała pętli zobacz czy masz poprawnie zadeklarowany początek i koniec, np. wydrukuj wszystkie elementy.

"""

print("For loop")
for i in range(1, 101):
    if i % 3 == 0:
        print(i)

print()
print("While loop (version1)")
number = 1
while True:
    if number > 100:
        break
    if number % 3 == 0:
        print(number)
    number += 1

print()
print("While loop (version2)")
number = 3
while True:
    if number > 100:
        break
    print(number)
    number += 3