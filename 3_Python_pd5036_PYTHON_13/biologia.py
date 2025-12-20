from collections import Counter
# zawartość pliku biologia.py
def opis_komorki():
    return "Komórka to podstawowa jednostka życi."

def licz_nukleotydy(sekwencja):
    sekwencja = sekwencja.upper()
    licznik = Counter(sekwencja)
    return {'A': licznik.get('A', 0),
            'T': licznik.get('T', 0),     
            'G': licznik.get('G', 0),
            'C': licznik.get('C', 0)}               



