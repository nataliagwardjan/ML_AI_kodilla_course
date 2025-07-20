"""
Zadanie 1
Pamiętasz zadanie z listą zakupów?

Załóżmy, że mamy do zrobienia zakupy spożywcze, potrzebujemy pójść do piekarni, w której kupujemy chleb, bułki oraz pączka. Poza tym po drodze wstąpimy też do warzywniaka, gdzie kupimy marchew, seler i rukolę.

W pliku, który właśnie utworzyliśmy:

zdefiniuj słownik zawierający listę zakupów, gdzie kluczem jest nazwa sklepu, a wartością lista przedmiotów, które chcesz kupić w danym sklepie.
Następnie za pomocą pętli for, przeiteruj po tym słowniku i wyświetl napis w postaci: Idę do <sklep> i kupuję tam <rzeczy>.
Dodatkowo, używając wbudowanych metod operacji na napisach, spowoduj, aby nazwy sklepów i towarów były wypisane wielką literą (sięgnij do oficjalnej dokumentacji, by odnaleźć taką funkcjonalność).
Na koniec, w ostatniej linii wypisz W sumie kupuję <X> produktów.. X to sumaryczna liczba towarów, które są na listach.
Twój program po uruchomieniu, powinien wyświetlić następujące informacje:

Lista zakupów
Idę do Piekarnia, kupuję tu następujące rzeczy: ['Chleb', 'Pączek', 'Bułki'].
Idę do Warzywniak, kupuję tu następujące rzeczy: ['Marchew', 'Seler', 'Rukola'].
W sumie kupuję 6 produktów.
"""

shopping_list = {
    'piekarnia': ['chleb', 'paczki', 'bulki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

number_of_products = 0
print("Lista zakupów")
for key, value in shopping_list.items():
    print(f"Idę do {key.title()}, kupuję tu następujące rzeczy: {[product.title() for product in value]}")
    number_of_products += len(value)
print(f"W sumie kupuje {number_of_products} produktów")