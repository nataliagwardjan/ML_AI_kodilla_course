"""
Zadanie 2
Napisz program, który:

Dla liczb z zakresu od 0 do 100, wyświetli te, które są podzielne przez 5.
W następnym wierszu wyświetli te liczby podniesione do potęgi 3.
Przesyłanie zadań
Zrób zrzuty ekranu z uruchomienia Twoich programów przez VSCode wraz z ich kodem źródłowym i wyślij je swojemu Mentorowi.

Wskazówka: Staraj się trzymać porządek w strukturze projektu i plików. Dobrym pomysłem będzie utrzymywanie każdego zadania jako osobnego pliku.

"""
list_of_numbers = []
for number in range(0, 101):
    if number % 5 == 0:
        list_of_numbers.append(number)
        print(number, end=", ")

print()
for number in list_of_numbers:
    print(number**3, end=", ")
