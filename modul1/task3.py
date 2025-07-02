"""
Utworzyć rysunki z gwazdek:

0
*
**
***
****
*****

1
* * * * * * * * * *
 * * * * * * * * * *
* * * * * * * * * *
 * * * * * * * * * *
* * * * * * * * * *
 * * * * * * * * * *
* * * * * * * * * *
 * * * * * * * * * *
* * * * * * * * * *
 * * * * * * * * * *


2
**
**
****
****
******
******
********
********

3
******
*****
****
***
**
*

"""

print("Pattern 0")
for i in range(1, 6):
    print(i * "*")

print()
print("Pattern 1")
for i in range(1, 11):
    line = ""
    if i % 2 == 0:
        line += " "
    for j in range(1, 11):
        line += "* "
    print(line)

# or

print("or")
for i in range(1, 11):
    if i % 2 == 0:
        print(" ", end="")
    for j in range(1, 11):
        print("* ", end="")
    print()

print()
print("Pattern 2")
for i in range(1, 5):
    for j in range(2):
        print(i * "**")



print()
print("Pattern 3")
n = 6
for i in range(1, n + 1):
    print((n + 1 - i) * "*")
