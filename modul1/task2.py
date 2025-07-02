"""
Mimo wielkich starań z Twojej strony szef nie był do końca zadowolony z przedstawionego raportu na temat serowych sprawunków. Zabrakło w nim kilku bardzo ważnych elementów, a przede wszystkim sumy wydatków.

Ponadto po wstępnej degustacji, szef nakazał dokupienie większej ilości sera. Obecnie masz 2 kg roqueforta, 3,5 kg parmezanu, 130 dag mozzarelli, 220 dag sera owczego, oraz po kilogramie pozostałych.

Po takiej uczcie, goście z pewnością docenią także deser – listek miętowy (200 g za 20 zł) [*] – link tylko dla ludzi o mocnych nerwach.

Stwórz nowy plik Pythona, wklej do niego kod z poprzedniego zadania, a następnie zmodyfikuj program, by uwzględnić nową masa produktów. Stwórz odpowiednie obliczenia w tekście, a na koniec przedstaw raport w takiej postaci:

Raport z zakupów:
Produkt, masa w kg, cena
Produkt, masa w kg, cena
...
Suma zł:
Nowy plik ponownie umieść na dysku Google lub Google Docs i udostępnij. Link do swojego kodu prześlij Mentorowi (Pamiętaj, by ustawić prawa dostępu do linka każdemu, kto ma link).
"""

# Version 1
roquefort_name = 'roquefort'
roquefort_weight = 2.0
roquefort_price = 12.5 * roquefort_weight
stilton_name = 'stilton'
stilton_weight = 1.0
stilton_price = 11.24 * stilton_weight
brie_name = 'brie'
brie_weight = 1.0
brie_price = 9.3 * brie_weight
gouda_name = 'gouda'
gouda_weight = 1.0
gouda_price = 8.55 * brie_weight
edam_name = 'edam'
edam_weight = 1.0
edam_price = 11.0 * edam_weight
parmezan_name = 'parmezan'
parmezan_weight = 3.5
parmezan_price = 16.5 * parmezan_weight
mozzarella_name = 'mozzarella'
mozzarella_weight = 1.3
mozzarella_price = 14.0 * mozzarella_weight
czechoslowacki_cheese_name = 'czechoslowacki ser z owczego mleka'
czechoslowacki_cheese_weight = 2.2
czechoslowacki_cheese_price = 122.32 * czechoslowacki_cheese_weight
mint_leaf_name = "liść mięty"
mint_leaf_weight = 0.2
mint_leaf_price = 20.0  # price for 200 g

total_price = roquefort_price + stilton_price + brie_price + gouda_price + edam_price + parmezan_price + mozzarella_price + czechoslowacki_cheese_price + mint_leaf_price

print("Report z zakupów:")
print("---------------------------")
print(f"Produkt: {roquefort_name}, masa: {roquefort_weight} kg, cena: {roquefort_price:.2f} zł")
print(f"Produkt: {stilton_name}, masa: {stilton_weight} kg, cena: {stilton_price:.2f} zł")
print(f"Produkt: {brie_name}, masa: {brie_weight} kg, cena: {brie_price:.2f} zł")
print(f"Produkt: {gouda_name}, masa: {gouda_weight} kg, cena: {gouda_price:.2f} zł")
print(f"Produkt: {edam_name}, masa: {edam_weight} kg, cena: {edam_price:.2f} zł")
print(f"Produkt: {parmezan_name}, masa: {parmezan_weight} kg, cena: {parmezan_price:.2f} zł")
print(f"Produkt: {mozzarella_name}, masa: {mozzarella_weight} kg, cena: {mozzarella_price:.2f} zł")
print(
    f"Produkt: {czechoslowacki_cheese_name}, masa: {czechoslowacki_cheese_weight} kg, cena: {czechoslowacki_cheese_price:.2f} zł")
print(
    f"Produkt: {mint_leaf_name}, masa: {mint_leaf_weight} kg, cena: {mint_leaf_price:.2f} zł")
print("---------------------------")
print(f"Suma: {total_price} zł")
print("---------------------------")
print()
print()

# Version 2
roquefort = {
    'name': roquefort_name,
    'weight': roquefort_weight,
    'price': roquefort_price
}
stilton = {
    'name': stilton_name,
    'weight': stilton_weight,
    'price': stilton_price
}
brie = {
    'name': brie_name,
    'weight': brie_weight,
    'price': brie_price
}
gouda = {
    'name': gouda_name,
    'weight': gouda_weight,
    'price': gouda_price
}
edam = {
    'name': edam_name,
    'weight': edam_weight,
    'price': edam_price
}
parmezan = {
    'name': parmezan_name,
    'weight': parmezan_weight,
    'price': parmezan_price
}
mozzarella = {
    'name': mozzarella_name,
    'weight': mozzarella_weight,
    'price': mozzarella_price
}
czechoslowacki_cheese = {
    'name': czechoslowacki_cheese_name,
    'weight': czechoslowacki_cheese_weight,
    'price': czechoslowacki_cheese_price
}
mint_leaf = {
    'name': mint_leaf_name,
    'weight': mint_leaf_weight,
    'price': mint_leaf_price
}

products = [roquefort, stilton, brie, gouda, edam, parmezan, mozzarella, czechoslowacki_cheese, mint_leaf]

total_price = 0.0

print("Report z zakupów:")
print("---------------------------")
for product in products:
    print(f"Produkt: {product['name']}, masa: {product['weight']} kg, cena: {product['price']:.2f} zł")
    total_price += product['price']
print(f"Suma: {total_price:.2f} zł")
print("---------------------------")
print()
print()