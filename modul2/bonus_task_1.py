"""
Oto dane, które musisz przekleić do swojego pliku.

exam_points = {
  "Mariusz":30,
  "Mateusz":55,
  "Marta":76,
  "Roman":30,
  "Arleta":59,
  "Adrian": 96,
  "Monika":91,
  "Andrzej":22,
  "Krzysztof":83,
  "Krystyna":93,
  "Piotr":44,
  "Dawid":10,
  "Agnieszka":15
}

failed_students = []
top_students = []
best_student = ("",0)
Zidentyfikuj najlepszych i najgorszych uczniów

Uczniowie klasy 1A pisali niedawno egzamin z języka angielskiego. Wyniki każdego z uczniów zostały umieszczone w słowniku przypisanym do zmiennej exam_points. Pomóż nauczycielowi w przygotowaniu listy uczniów, którzy:

Nie zdali egzaminu. Są to wszyscy uczniowie z oceną niedostateczny. Przypisz ich do zmiennej failed_students Zdali egzamin śpiewająco! Są to wszyscy uczniowie z oceną 'bardzo dobry'. Przypisz ich do zmiennej top_students Nauczyciel chciałby też znać imię najlepszego ucznia oraz liczbę punktów, jaką uzyskał podczas egzaminu. Zapisz tę informację w postaci krotki, której pierwszą wartością będzie imię ucznia, a drugą wartością będzie liczba punktów. Przypisz tę krotkę do zmiennej best_student.

Skala ocen z egzaminu:

0 - 45 niedostateczny 46 - 60 dopuszczający 61 - 75 dostateczny 76 - 90 dobry 91 - 100 bardzo dobry
"""


exam_points = {
  "Mariusz":30,
  "Mateusz":55,
  "Marta":76,
  "Roman":30,
  "Arleta":59,
  "Adrian": 96,
  "Monika":91,
  "Andrzej":22,
  "Krzysztof":83,
  "Krystyna":93,
  "Piotr":44,
  "Dawid":10,
  "Agnieszka":15
}

failed_students = []
top_students = []
best_student = ("",0)

for student, result in exam_points.items():
    _, best_result = best_student
    if result > best_result:
        best_student = (student, result)
    if result <= 45:
        failed_students.append(student)
    elif result > 90:
        top_students.append(student)

print("Students results")
print("All students")
for student, result in exam_points.items():
    print(f"{student}, result {result}")


print("Failed students")
print(failed_students)
print("Top students")
print(top_students)
print("Best student")
print(best_student)