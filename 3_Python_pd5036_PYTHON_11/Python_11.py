from pyclbr import Class


class Organizm:
    def __init__(self, nazwa, rodzaj):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
    
    def opisz(self):
        return f"nazwa {self.nazwa}, rodzaj {self.rodzaj}"

organizm1 = Organizm("Y. pestis", "bakteria")
print(organizm1.opisz())

class Bakteria(Organizm):
    def __init__(self, nazwa, rodzaj, kształt):
        super().__init__(nazwa, rodzaj)
        self.kształt = kształt

    def opisz1(self):
        return f"nazwa {self.nazwa}, rodzaj {self.rodzaj}, kształt {self.kształt}"

organizm2 = Bakteria("Y. pestis", "bakteria", "pałeczka")
print(organizm2.opisz1())

class Organizm:
    def transkrybuj(self, sekwnecja_dna):
        return sekwnecja_dna.replace("T", "U")
print(Organizm().transkrybuj("ATCGTTA"))    
    