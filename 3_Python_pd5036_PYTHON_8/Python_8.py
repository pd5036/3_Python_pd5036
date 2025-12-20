sekwencja_dna = ['A', 'T', 'G', 'C', 'A', 'T', 'G', 'G']
zasady_azotowe = ('Adenina', 'Tymina', 'Cytozyna', 'Guanina')
print("Sekwencja DNA:", sekwencja_dna[0], sekwencja_dna[-1])
pierwsza_zasada = zasady_azotowe[0] # "Adenina"
ostatnia_zasada = zasady_azotowe[-1]
print(pierwsza_zasada, ostatnia_zasada)
sekwencja_dna.insert(5, 'C')
print("Zaktualizowana sekwencja DNA:", sekwencja_dna)
sekwencja_dna.append('A')
print("Dodana zasada do sekwencji DNA:", sekwencja_dna)
for nukleotyd in sekwencja_dna:
    print(nukleotyd)
for zasada in zasady_azotowe:
    print(zasada)
pirymidyny = [z for z in sekwencja_dna if z in ['C', 'T']]
print("Pirimidyny w sekwencji DNA:", pirymidyny)