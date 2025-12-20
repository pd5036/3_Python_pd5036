
Fragment_dna = "ATGCGTACGTTAGC"
Fragment_dna2 = 'GCTAGCTAGCTA'
Fragment_dna_pusty = ""
czy_sekwencja_jest_pełna = len(Fragment_dna) > 0 
print("Czy sekwencja DNA jest pełna?", czy_sekwencja_jest_pełna) # Wynik: True
wynik = bool(Fragment_dna_pusty) # Zwróci False, ponieważ 'Fragment_dna_pusty' jest pusty
print("fragment DNA jest pełny:", wynik) # Wynik: False

liczba_nukleotydow = 3300000000
liczba_kodonow = liczba_nukleotydow // 3
reszta_nukleotydow = liczba_nukleotydow % 3
print(f"Z {liczba_nukleotydow} nukleotydów można utworzyć {liczba_kodonow} pełnych kodonów.")
print(f"Pozostaje {reszta_nukleotydow} nukleotydów.")

suma_fragmentow = Fragment_dna + Fragment_dna2 + Fragment_dna_pusty
print("Suma nukleotydów w łańcuchu DNA:", (suma_fragmentow),  len(suma_fragmentow)) # Wynik
mutacje = "CTA"
liczba_mutacji = suma_fragmentow.find(mutacje)
print(f"Liczba mutacji '{mutacje}' w sekwencji DNA:", liczba_mutacji) # Wynik
liczba_mutacji **= 4
liczba_mutacji //= 2
liczba_mutacji *= 3
print("Zaktualizowana liczba mutacji:", liczba_mutacji)
liczba_nukleotydów1 = len(Fragment_dna)
liczba_nukleotydow2 = len(Fragment_dna2)
print("Czy Fragment_dna2 jest dłuższy niż Fragment_dna1?", liczba_nukleotydów1 < liczba_nukleotydow2)
print("Czy oba fragmenty mają tę samą długość?", liczba_nukleotydów1 == liczba_nukleotydow2)
print("Czy Fragment_dna1 jest dłuższy niż Fragment_dna2?", liczba_nukleotydów1 > liczba_nukleotydow2)

