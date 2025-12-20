import pandas as pd
import numpy as np
# Dane biologiczne (ekspresja genów w trzech próbkach)
dane = {
'Gen': ['GenA', 'GenB', 'GenC', 'GenD'],
'Proba1': [5.1, 2.3, np.nan, 4.4],
'Proba2': [3.2, 4.5, 3.9, np.nan],
'Proba3': [6.3, 5.6, np.nan, 6.6]
} #Tworzenie DataFrame z danych
df = pd.DataFrame(dane)
print(df)
# Sprawdzanie, które wartości są brakujące
print(df.isnull())
# Usunięcie wierszy z brakującymi danymi
df_bez_nan = df.dropna()
print("DataFrame bez brakujących wartości:\n", df_bez_nan)
# Wypełnienie brakujących wartości średnią z danej kolumny
df_wypelniony = df.fillna(df[['Proba1', 'Proba2', 'Proba3']].mean())        
print("DataFrame wypełniony średnią:\n", df_wypelniony)
# Wyciągnięcie danych dla genu 'GenA'
genA = df[df['Gen'] == 'GenA']
print("Dane dla genu GenA:\n", genA)
# Obliczenie średniej ekspresji dla każdej próbki
srednia_ekspresja = df[['Proba1', 'Proba2', 'Proba3']].mean()
print("Średnia ekspresja w próbkach:\n", srednia_ekspresja)
# Filtrowanie genów, które mają ekspresję większą niż 4 w próbce 1
wysoka_ekspresja = df[df['Proba1'] > 4]
print("Geny o wysokiej ekspresji w próbce 1:\n", wysoka_ekspresja)
# Zapis danych do pliku CSV
df.to_csv('wynik.csv', index=False)
print("Dane zapisane do pliku wynik.csv")       
