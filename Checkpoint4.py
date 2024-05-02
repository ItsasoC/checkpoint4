# Checkpoint4

# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

list1 = ["Donosti", "Gasteiz", "Bilbo"]
print(list1)

tuple1 = ("titulo","subtitulo","resumen")
print(tuple1)

float1 = 1.99
print(float1)

integer1 = 5
print(integer1)

from decimal import Decimal
decimal1 = Decimal(2.6)
print(decimal1)

dictionary1 = {
    "nombre": "Itsaso",
    "apellido1": "Carmona",
    "apellido2": "Igartua",
}
print(dictionary1)

# Exercise 2: Round your float up.
import math
print(math.ceil(float1))

# Exercise 3: Get the square root of your float.
print(math.sqrt(float1))

#Exercise 4: Select the first element from your dictionary.
print(dictionary1["nombre"])

# Exercise 5: Select the second element from your tuple.
print(tuple1[1])

# Exercise 6: Add an element to the end of your list.
list1.append("Oñati")
print(list1)

# Exercise 7: Replace the first element in your list.
list1[0] = "Baiona"
print(list1)

# Exercise 8: Sort your list alphabetically.

# Opcion1: no modificar la variable, solo ver ordenada
print(sorted(list1))
# Opcion2: primero ordenar y luego ver la variable
list1.sort()
print(list1)

# Exercise 9: Use reassignment to add an element to your tuple.
tuple1 += ("texto",)
print(tuple1)