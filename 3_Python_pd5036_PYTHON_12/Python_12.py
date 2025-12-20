try:
    with open("sekwencja.txt", "r") as plik:
        zawartosc = plik.read()
        print(zawartosc)
except FileNotFoundError:
    print("Nie znaleziono pliku z sekwencją DNA.")

sekwencje = input("Podaj sekwencje DNA:")
print("Podano gatunek:", sekwencje)

def sprawdz_sekwencje_dna(sekwencje):
    dozwolone_nukleotydy = set('ATCG')
    for nukleotyd in sekwencje.upper():
        if nukleotyd not in dozwolone_nukleotydy:
            return False
    return True

if sprawdz_sekwencje_dna(sekwencje):
    print("Sekwencja jest prawidłowa.")
    with open("nowa_sekwencja.txt", "w") as plik:
        plik.write(sekwencje + "\n")        
    print("Sekwencja została zapisana do pliku.")
else:
    print("Sekwencja zawiera nieprawidłowe nukleotydy.")



