import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Przygotowanie danych: Ekspresja trzech genów w czterech próbkach
geny = ['GenA', 'GenB', 'GenC']
proby = ['Proba1', 'Proba2', 'Proba3']
ekspresja = np.array([
[5.1, 2.3, 7.8], # Ekspresja GenA
[3.2, 4.5, 6.1], # Ekspresja GenB
[4.8, 5.5, 3.9] # Ekspresja GenC
])
# 1. Wykres liniowy (line plot)
# Rysowanie wykresu pokazującego zmiany ekspresji genów w trzech próbkach
plt.figure(figsize=(6, 4))
for i, gen in enumerate(geny):
    plt.plot(proby, ekspresja[i], marker='o', label=gen)
plt.title('Wykres liniowy ekspresji genów w próbkach')
plt.xlabel('Próbki')
plt.ylabel('Ekspresja')
plt.legend(title="Geny")
plt.grid(True) # Dodanie siatki
plt.show()
# 2. Wykres słupkowy (bar plot)
# Porównanie ekspresji każdego genu w poszczególnych próbkach
plt.figure(figsize=(6, 4))
width = 0.2 # Szerokość słupków
x = np.arange(len(proby)) # Pozycje próbek na osi X
for i, gen in enumerate(geny):
    plt.bar(x + i * width, ekspresja[i], width, label=gen)
plt.xticks(x + width, proby) # Etykiety osi X
plt.title('Wykres słupkowy ekspresji genów w próbkach')
plt.xlabel('Próbki')
plt.ylabel('Ekspresja')
plt.legend(title="Geny")
plt.show()
plt.savefig('Porównanie_ekspresji_genów.png')   
# 3. Wykres rozrzutu (scatter plot)
# Wykres rozrzutu porównujący ekspresję dwóch genów (GenA i GenB)
plt.figure(figsize=(6, 4))
plt.scatter(ekspresja[0], ekspresja[1], color='green', marker='x')
plt.title('Wykres rozrzutu ekspresji GenA i GenB')
plt.xlabel('Ekspresja GenA')
plt.ylabel('Ekspresja GenB')
plt.grid(True)
plt.show()