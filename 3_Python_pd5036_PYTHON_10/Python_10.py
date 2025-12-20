def charakterystyka_białka(*, sekwencja, masa, pI):
    return (
        f"Charakterystyka białka:\n"
        f"- Sekwencja: {sekwencja}\n"
        f"- Długość: {len(sekwencja)} aa\n"
        f"- Masa: {masa} Da\n"
        f"- Punkt izoelektryczny (pI): {pI}\n"
    )

def sumuj_cechy_białek(**białka):
    # Każda wartość ma format: (sekwencja, masa, pI)
    suma_mas = 0
    suma_pI = 0
    liczba = 0

    for nazwa, (sekwencja, masa, pI) in białka.items():
        suma_mas += masa
        suma_pI += pI
        liczba += 1

    srednie_pI = suma_pI / liczba if liczba > 0 else 0
    return suma_mas, srednie_pI


print(charakterystyka_białka(sekwencja="ACDEFGHIK", masa=12500, pI=6.8))

wynik = sumuj_cechy_białek(
    białko1=("AGDHD", 15000, 7.2),
    białko2=("ACDEFGHIK", 20500, 6.5),
    białko3=("MAKVTS", 10000, 8.0)
)


print("Suma mas:", wynik[0], "Da")
print("Średnie pI:", wynik[1])
