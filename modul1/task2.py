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


header = f"{'Nazwa sera':<{len(czechoslowacki_cheese_name) + 2}} | {'masa, kg':>10} | {'cena, zł':>10}"
line = "-" * len(header)
sum_price_str = f"{total_price:>10.2f}"
sum_line = f"{'Suma':<{(len(czechoslowacki_cheese_name) + 2) + 3}}{' ' * 10} | {sum_price_str}"

message = f"""
{header}
{line}
{roquefort_name:<{len(czechoslowacki_cheese_name) + 2}} | {roquefort_weight:>10.1f} | {roquefort_price:>10.2f}
{brie_name:<{len(czechoslowacki_cheese_name) + 2}} | {brie_weight:>10.1f} | {brie_price:>10.2f}
{stilton_name:<{len(czechoslowacki_cheese_name) + 2}} | {stilton_weight:>10.1f} | {stilton_price:>10.2f}
{gouda_name:<{len(czechoslowacki_cheese_name) + 2}} | {gouda_weight:>10.1f} | {gouda_price:>10.2f}
{edam_name:<{len(czechoslowacki_cheese_name) + 2}} | {edam_weight:>10.1f} | {edam_price:>10.2f}
{parmezan_name:<{len(czechoslowacki_cheese_name) + 2}} | {parmezan_weight:>10.1f} | {parmezan_price:>10.2f}
{mozzarella_name:<{len(czechoslowacki_cheese_name) + 2}} | {mozzarella_weight:>10.1f} | {parmezan_price:>10.2f}
{czechoslowacki_cheese_name:<{len(czechoslowacki_cheese_name) + 2}} | {czechoslowacki_cheese_weight:>10.1f} | {czechoslowacki_cheese_price:>10.2f}
{line}
{sum_line}
"""

print(message)
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

rows = []

for product in products:
    mass_str = f"{product['weight']:>10.1f}"
    price_str = f"{product['price']:>10.2f}"
    rows.append(f"{product['name']:<{len(czechoslowacki_cheese_name) + 2}} | {mass_str} | {price_str}")
    total_price += product['price']

header = f"{'Nazwa sera':<{len(czechoslowacki_cheese_name) + 2}} | {'masa, kg':>10} | {'cena, zł':>10}"
line = "-" * len(header)
sum_price_str = f"{total_price:>10.2f}"
sum_line = f"{'Suma':<{(len(czechoslowacki_cheese_name) + 2) + 3}}{' ' * 10} | {sum_price_str}"

message = "\n".join([header, line] + rows + [line, sum_line])

print(message)
print()