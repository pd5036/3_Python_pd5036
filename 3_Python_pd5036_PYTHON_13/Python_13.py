import os   
import datetime
import biologia

print(biologia.opis_komorki())

sekwencja_dna = "AGCTTAGCTAAGGCTA"
liczba_nukleotydow = biologia.licz_nukleotydy(sekwencja_dna)

data_i_czas = datetime.datetime.now()
print("Aktualna data i czas:", data_i_czas)

nowy_katalog = "dane_bio"
if not os.path.exists(nowy_katalog):
    os.makedirs(nowy_katalog)
    print(f'Utworzono katalog: {nowy_katalog}')
else:
    print(f'Katalog już istnieje: {nowy_katalog}')  

sciezka_do_pliku = os.path.join(nowy_katalog, "nukleotydy.txt")

with open(sciezka_do_pliku, 'w') as plik:
    plik.write(f"Data i czas utworzenia pliku: {data_i_czas}\n\n")  
    plik.write("Liczba nukleotydów w sekwencji DNA:" + "\n")
    for nukleotyd, liczba in liczba_nukleotydow.items():
        plik.write(f"{nukleotyd}: {liczba}\n")  
print(f"Plik '{sciezka_do_pliku}' został utworzony i zapisany.")