aminokwasy = {'Glicyna', 'Alanina', 'Walina', 'Leucyna'}
aminokwasy1 = {'Seryna', 'Treonina', 'Cysteina', 'Alanina'}
geny = {
    'LUM-X1':  'Lucyferyna stresowa', 
    'THERM-V': 'Lipaza kriogeniczna',
    'NEURO-SYNC': 'Receptory synaptyczne',
    'PLASTO-ZYME': 'Karbonaza syntetyczna'
}
print(geny["LUM-X1"]) # Wyświetli "Lucyferyna stresowa"
print(geny.keys()) # Wyświetli listę kluczy
print(geny.values()) # Wyświetli listę wartości
print(geny.items()) # Wyświetli listę par klucz-wartość
aminokwasy.add('Seryna')        
print(aminokwasy)
geny['CYTO-REDOX'] = 'Enzym redoks'
print(geny)
if 'Glicyna' in aminokwasy:
    print("Glicyna jest w zbiorze aminokwasów")
if Lum_X1 := geny.get('LUM-X1'):
    print(f"LUM-X1 koduje: {Lum_X1}")   
aminokwasy.remove('Walina')
print(aminokwasy)
for gen in geny:
    print(gen)
for gen, funkcja in geny.items():
    print(f"{gen}: {funkcja}")  
if len(aminokwasy) > 3:
    print("Zbiór aminokwasów zawiera więcej niż 3 elementy.") 
else:
    print("Zbiór aminokwasów zawiera 3 lub mniej elementów.")     
for gen in geny:
    if gen == 'THERM-V':
        print(f"{gen} jest kluczem w słowniku geny")
wynik_połączenia = aminokwasy.union(aminokwasy1)
print(wynik_połączenia) # Wyświetli zbiór zawierający wszystkie unikalne aminokwasy z obu zbiorów