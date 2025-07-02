"""
Znajdź liczbę poszczególnych samogłosek.
Do zmiennej text przypisano kultowy fragment z filmu "Żywot Briana" autorstwa ekipy Monty Pythona.

Wykorzystując utworzone zmienne:

number_of_a number_of_e number_of_i number_of_o number_of_u number_of_y policz ile poszczególnych samogłosek możemy znaleźć w cytacie przypisanym do zmiennej text.
"""

text = """– Czemu tak ciągle gadasz o kobietach, Stan?
– Bo chcę zostać kobietą. Chcę być kobietą. Chce żebyście od dziś mówili na mnie „Loretta”. To moje niezbywalne prawo jako mężczyzny.
– Ale dlaczego chcesz zostać Lorettą, Stan?
– Bo chcę mieć dzieci.
– Dzieci?
– Każdy mężczyzna ma prawo mieć dzieci, jeśli chce.
– Przecież ty nie możesz mieć dzieci!
– Nie prześladuj mnie!
– Nie prześladuję cię, Stan! Nie masz macicy! Gdzie będziesz trzymał swojego embriona? W pudełku?
– Mam pomysł! Przyjmijmy, że Stan nie może póki co mieć dzieci, gdyż nie ma macicy, co nie jest niczyją winą, nawet Rzymian, ale musimy przyznać, że ma prawo do dzieci!
– Świetnie, Judith! Będziemy walczyć z ciemiężycielami…
– Przepraszam.
– A po co?
– Co po co?
– Po co walczyć o jego prawo do posiadania dzieci…
– To symbol naszej beznadziejnej walki z najeźdźcą.
– Symbol jego beznadziejnej walki z rzeczywistością."""

number_of_a = 0
number_of_e = 0
number_of_i = 0
number_of_o = 0
number_of_u = 0
number_of_y = 0

for letter in text:
    if letter == 'a':
        number_of_a += 1
    if letter == 'e':
        number_of_e += 1
    if letter == 'i':
        number_of_i += 1
    if letter == 'o':
        number_of_o += 1
    if letter == 'u':
        number_of_u += 1
    if letter == 'y':
        number_of_y += 1

print(f"Number of 'a': {number_of_a}")
print(f"Number of 'e': {number_of_e}")
print(f"Number of 'i': {number_of_i}")
print(f"Number of 'o': {number_of_o}")
print(f"Number of 'u': {number_of_u}")
print(f"Number of 'y': {number_of_y}")