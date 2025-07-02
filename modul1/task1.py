"""
Szef organizuje przyjęcie dla klientów i wysłał Cię do sklepu z serami. Wiadomo jak to jest z
tego typu instytucjami [*], czasami półki świecą pustkami, ale powiedzmy, że po długich
poszukiwaniach udało Ci się znaleźć dobrze wyposażony i kupić wszystko, co potrzeba
(oprócz mocno przechodzonego camemberta).
Nie bojąc się stringów ani ich formatowania, skorzystaj z dotychczasowej wiedzy i stwórz
raport. Zaskocz swojego szefa rzeczową listą zakupów wraz z cenami.
W Twoim koszyku znalazł się kilogram każdego z tych serów: roquefort (12,50 zł), stilton
(11,24 zł), brie (9,30 zł), gouda (8,55 zł), edam (11 zł), parmezan (16,50 zł), mozzarella (14
zł) oraz hit – czechosłowacki ser z owczego mleka (122,32 zł).
Stwórz odpowiednie zmienne, zarówno dla produktów, jak i cen. Umieść wszystko w jednym
tekście i użyj odpowiedniego formatowania. Pamiętaj, że ceny w Polsce zwykło się podawać
z dwoma miejscami dziesiętnymi po przecinku (w Pythonie, zgodnie z anglosaską tradycją,
używamy kropki zamiast przecinka, więc w kodzie napiszemy 2.49, a nie 2,49).
"""

roquefort_name = 'roquefort'
roquefort_weight = 1.0
roquefort_price = 12.5 * roquefort_weight
stilton_name = 'stilton'
stilton_weight = 1.0
stilton_price = 11.24 * stilton_weight
brie_name = 'brie'
brie_weight = 1.0
brie_price = 9.3 * brie_weight
gouda_name = 'gouda'
gouda_weight = 1.0
gouda_price = 8.55 * gouda_weight
edam_name = 'edam'
edam_weight = 1.0
edam_price = 11.0 * edam_weight
parmezan_name = 'parmezan'
parmezan_weight = 1.0
parmezan_price = 16.5 * parmezan_weight
mozzarella_name = 'mozzarella'
mozzarella_weight = 1.0
mozzarella_price = 14.0 * mozzarella_weight
czechoslowacki_cheese_name = 'czechoslowacki ser z owczego mleka'
czechoslowacki_cheese_weight = 1.0
czechoslowacki_cheese_price = 122.32 * czechoslowacki_cheese_weight

message = f"""
Report
-----------------------------------------
Ser: {roquefort_name}, ilość: {roquefort_weight} kg, cena: {roquefort_price} zł,
Ser: {brie_name}, ilość: {brie_weight} kg, cena: {brie_price} zł,
Ser: {stilton_name}, ilość: {stilton_weight} kg, cena: {stilton_price} zł,
Ser: {brie_name}, ilość: {brie_weight} kg, cena: {brie_price} zł,
Ser: {gouda_name}, ilość: {gouda_weight} kg, cena: {gouda_price} zł,
Ser: {edam_name}, ilość: {edam_weight} kg, cena: {edam_price} zł,
Ser: {parmezan_name}, ilość: {parmezan_weight} kg, cena: {parmezan_price} zł,
Ser: {mozzarella_name}, ilość: {mozzarella_weight} kg, cena: {mozzarella_price} zł,
Ser: {czechoslowacki_cheese_name}, ilość: {czechoslowacki_cheese_weight} kg, cena: {czechoslowacki_cheese_price} zł
"""

print(message)