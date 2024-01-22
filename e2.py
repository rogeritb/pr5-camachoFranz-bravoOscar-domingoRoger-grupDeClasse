"""
Descripcion:
Programa que generi una llista de 100 nombres aleatoris entre 1 i 50.
Obtenir la mitja dels nombres que es troben a les posicions parelles i la mitja del nombre de les posicions senars.
"""

import random

nombres = [random.randint(1, 9) for _ in range(100)]

mitjana_parelles = 0
mitjana_senars = 0

for i in range(100):
    if i % 2 == 0:  # Posicions parelles
        mitjana_parelles += nombres[i]
    else:  # Posicions senars
        mitjana_senars += nombres[i]

mitjana_parelles /= 50
mitjana_senars /= 50

print("Llista de nombres aleatoris:", nombres)
print("Mitjana de les posicions parelles:", mitjana_parelles)
print("Mitjana de les posicions senars:", mitjana_senars)
