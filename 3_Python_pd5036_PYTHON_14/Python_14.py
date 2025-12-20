import numpy as np

macierz_ekspresji = np.array([[5.0, 2.5, 7.0],
[3.2, 4.0, 6.0],
[8.1, 9.3, 2.5],
[4.5, 5.7, 6.9]])

print("Oryginalna macierz ekspresji:")
print(macierz_ekspresji)

# Zwiększenie wszystkich wartości ekspresji o 5%
zmnieniona_macierz_ekspresji = macierz_ekspresji * 1.05 
print("Zmieniona macierz ekspresji (zwiększona o 5%):")
print(zmnieniona_macierz_ekspresji)     
# Obliczenie średniej ekspresji dla każdego genu (wiersza)
srednia_ekspresja_genow = np.mean(macierz_ekspresji, axis=1)
print("Średnia ekspresja dla każdego genu:", srednia_ekspresja_genow)        
# Obliczenie sumę ekspresji genów dla każdej próby (kolumny)
suma_ekspresji_prob = np.sum(macierz_ekspresji, axis=0)
print("Suma ekspresji genów dla każdej próby:", suma_ekspresji_prob)

macierz_ekspresji_NaN = np.array([[5.0, 2.5, 7.0],
[3.2, 4.0, 6.0],
[8.1, np.nan, 2.5],
[4.5, 5.7, np.nan]])
print("Macierz ekspresji z NaN:")
print(macierz_ekspresji_NaN)
# Obliczenie średniej ekspresji dla każdego genu, ignorując NaN
srednia_ekspresja_genow_NaN = np.nanmean(macierz_ekspresji_NaN, axis=1)
print("Średnia ekspresja dla każdego genu (ignorując NaN):", srednia_ekspresja_genow_NaN)


