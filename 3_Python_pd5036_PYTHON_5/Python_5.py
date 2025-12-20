# typ tekstowy, reprezentowany przez klasę str:
x = str("ATCGGGGGTACATA")
print(x, type(x))
y = list(x)
print(y, type(y))
z = range(1, (y)+1)
print("pozycje_nukleotydów", list(z))