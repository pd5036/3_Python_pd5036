sekwencja_dna1 = "ATCGTGCAAACTGGGGGGAAAATCG"
sekwencja_dna2 = "GCTTGCGAGAGTAGTGCAGCCCACA"
sekwencja_dna_polaczona = sekwencja_dna1 + sekwencja_dna2
print(sekwencja_dna_polaczona) # "ATCGTGCAAACTGGGGGGAAAATCGGCTTGCGAGAGTAGTGCAGCCCACA"
fragment1 = sekwencja_dna_polaczona[5:15]
print("wyznaczony:", fragment1) # "GCAAACTGGG"
pozycja_AAA = sekwencja_dna_polaczona.find("AAA")
print("pozycja AAA:", pozycja_AAA) # 7
liczba_T = sekwencja_dna_polaczona.count("T")
print("liczba T:", liczba_T) # 8
opis = f"W sekwenji wykrytio {fragment1} liczba AAA {pozycja_AAA} liczba T wynosi {liczba_T}"
print(opis) # "W sekwenji wykrytio GCAAACTGGG liczba T wynosi 8"
print(f"wyniki:\n\tw sekwencji wyrkryto: {fragment1}\n\tliczba_AAA: {pozycja_AAA}\n\tliczba_T: {liczba_T}")