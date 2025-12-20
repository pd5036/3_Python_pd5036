from Bio import Entrez
from Bio import SeqIO
from Bio.Align import PairwiseAligner
# Ustawienie adresu email
Entrez.email = "lukasz.krzowski@wat.edu.pl"
# Pobieranie sekwencji GenBank o podanym ID
handle = Entrez.efetch(db="nucleotide", id="JX669568", rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle1 = Entrez.efetch(db="nucleotide", id="JX669571", rettype="gb", retmode="text")
record1 = SeqIO.read(handle1, "genbank")
# Wyświetlenie podstawowych informacji o sekwencji
print("ID:", record.id)
print("Opis:", record.description)
print("Sekwencja:", record.seq[:50], "...")
print("ID:", record1.id)
print("Opis:", record1.description)
print("Sekwencja:", record1.seq[:50], "...")

seq1 = record
seq2 = record1
# Utworzenie obiektu alignera i ustawienie odpowiednich parametrów      
aligner = PairwiseAligner()
aligner.mode = 'global'     
# Dopasowanie sekwencji za pomocą algorytmu Needleman-Wunsch
alignments = aligner.align(seq1.seq, seq2.seq)  
# Wyświetlanie najlepszego dopasowania
best_alignment = alignments[0]
print("Najlepsze dopasowanie:", best_alignment)

alignments = aligner.align(seq1, seq2)
for alignment in alignments:
    print(f"Wynik: {alignment.score:.1f}")
    print(alignment)