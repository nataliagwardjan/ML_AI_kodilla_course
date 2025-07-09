"""
Na potrzebę tego zadania musisz utworzyć drugi plik i przekleić do niego poniższy kod:

names = ['Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz', 'Edward', 'Piotr', 'Jan', 'Denis', 'Amir',
'Igor', 'Borys', 'Robert', 'Ariel', 'Kuba', 'Rafał', 'Mateusz', 'Emanuel', 'Alfred', 'Artur', 'Jakub',
'Ludwik', 'Bolesław', 'Remigiusz', 'Martin', 'Dobromił', 'Mariusz', 'Amadeusz', 'Łukasz', 'Bolesław', 'Amir',
'Artur', 'Albert', 'Olgierd', 'Alek', 'Kordian', 'Julian', 'Anastazy', 'Emanuel', 'Józef']

name_dict = {}
Stwórz słownik imion Do zmiennej names została przypisana lista imion męskich.

Stwórz słownik, którego kluczami będą pierwsze litery imion w liście names, a wartościami będą wszystkie imiona, które zaczynają się na daną literę.

Słownik przypisz do zmiennej name_dict.

Na przykład:

name_dict['P'] powinien zwracać imiona: Paweł, Piotr


"""

names = ['Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz', 'Edward', 'Piotr', 'Jan', 'Denis', 'Amir',
'Igor', 'Borys', 'Robert', 'Ariel', 'Kuba', 'Rafał', 'Mateusz', 'Emanuel', 'Alfred', 'Artur', 'Jakub',
'Ludwik', 'Bolesław', 'Remigiusz', 'Martin', 'Dobromił', 'Mariusz', 'Amadeusz', 'Łukasz', 'Bolesław', 'Amir',
'Artur', 'Albert', 'Olgierd', 'Alek', 'Kordian', 'Julian', 'Anastazy', 'Emanuel', 'Józef']

name_dict = {}

for name in names:
    set_of_names = name_dict.setdefault(name[0], set())
    set_of_names = set_of_names | {name}
    name_dict[name[0]] = set_of_names

print("Dictionary of names")
for letter, names in name_dict.items():
    print(f"{letter}:", end=" ")
    for name in names:
        print(f"{name}", end=", ")
    print()