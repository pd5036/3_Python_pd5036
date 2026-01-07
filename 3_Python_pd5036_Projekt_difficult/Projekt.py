import os
import subprocess
from Bio import AlignIO
from Bio import Phylo
from Bio.Seq import Seq
from Bio.Align import MultipleSeqAlignment
from Bio import Entrez
from Bio import SeqIO  
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from collections import Counter
from Bio.Align import AlignInfo
from Bio.SeqRecord import SeqRecord
import Bio.Blast.NCBIWWW as NCBIWWW
import Bio.Blast.NCBIXML as NCBIXML 
import matplotlib.pyplot as plt

#zapisywanie email i api key do pliku
def get_user_credentials():
    if os.path.exists("user_data.txt"):
        with open("user_data.txt", "r") as f:
            lines = f.readlines()
            email = lines[0].strip()
            api_key = lines[1].strip()
    else:
        email = input("Podaj swój email dla NCBI: ")
        api_key = input("Podaj swój NCBI API KEY: ")
        with open("user_data.txt", "w") as f:
            f.write(f"{email}\n{api_key}")
    return email, api_key

Entrez.email, Entrez.api_key = get_user_credentials()

# Pobieranie rekordów na podstawie taxid
taxid = input("Enter taxid id: ").strip()   
query = f"txid{taxid}[Organism:exp]"
print("Szukanie rekordów w NCBI...")
handle = Entrez.esearch(db="nucleotide", term=query, retmax=50)
record = Entrez.read(handle)
handle.close()  
idlist = record["IdList"]

# Jeśli brak rekordów, zakończ program
if not idlist:
    print("Brak rekordów dla podanego taxid.")
    exit()  


# Liczenie wystąpień genów
gene_counts = {}
fetch_handle = Entrez.efetch(db="nucleotide", id=idlist, rettype="gb", retmode="text")
records = list(SeqIO.parse(fetch_handle, "genbank"))    

# Iteracja przez rekordy i cechy genów
for seq_record in records:
    for feature in seq_record.features:
        if feature.type == "gene":
            gene_name = feature.qualifiers.get("gene", [""])[0] 
            gene_counts[gene_name] = gene_counts.get(gene_name, 0) + 1
fetch_handle.close()

# Wyświetlanie liczby wystąpień genów
print("Liczba wystąpień genów:")
for gene, count in gene_counts.items():
    print(f"{gene}: {count}")   
selected_gene = input("Wybierz gen do analizy: ").strip()
fasta_records = []
fetch_handle = Entrez.efetch(db="nucleotide", id=idlist, rettype="gb", retmode="text")
records = list(SeqIO.parse(fetch_handle, "genbank"))    
print(f"Rekordy zawierające gen {selected_gene}:")

# Wyświetlanie rekordów zawierających wybrany gen

for seq_record in records:
    for feature in seq_record.features:
        if feature.type == "gene" and feature.qualifiers.get("gene", [""])[0] == selected_gene:
            print(f"ID: {seq_record.id}, Opis: {seq_record.description}")
            break       
fetch_handle.close()

# Zapis sekwencji wybranego genu do pliku FASTA
fasta_records = []
for seq_record in records:
    for feature in seq_record.features:
        if feature.type == "gene" and feature.qualifiers.get("gene", [""])[0] == selected_gene:
            fasta_record = SeqRecord(feature.location.extract(seq_record.seq), id=seq_record.id, description=seq_record.description)
            fasta_records.append(fasta_record)
            break
SeqIO.write(fasta_records, f"{selected_gene}_sequences.fasta", "fasta")

print("\nZapisano sekwencje do pliku FASTA.")
print(f"Liczba zapisanych sekwencji: {len(fasta_records)}")

# sprawdzanie długości sekwencji
lengths = [len(record.seq) for record in fasta_records] 
if lengths:
    print(f"Długość najkrótszej sekwencji: {min(lengths)}")
    print(f"Długość najdłuższej sekwencji: {max(lengths)}")
    avg_length = sum(lengths) / len(lengths)
    print(f"Średnia długość sekwencji: {avg_length:.2f}")



# Tworzenie wielokrotnego wyrównania sekwencji
print("\nTworzenie wielokrotnego wyrównania sekwencji...")
alignment = MultipleSeqAlignment(fasta_records)
consensus_sequence = "" 
for i in range(alignment.get_alignment_length()):
    column = alignment[:, i]
    most_common = max(set(column), key=column.count)
    consensus_sequence += most_common   
print("\nSekwencja konsensusowa:")
print(consensus_sequence)

# Zapis sekwencji konsensusowej do pliku FASTA
with open(f"{selected_gene}_consensus.fasta", "w") as f:
    f.write(f">Consensus sequence for {selected_gene}\n")
    f.write(consensus_sequence)
print(f"\nZapisano sekwencję konsensusową do pliku {selected_gene}_consensus.fasta")

# Wykonanie  BLASTa
print("\nWykonywanie BLASTa...")  
result_handle = NCBIWWW.qblast("blastn", "nt", consensus_sequence)
blast_records = NCBIXML.read(result_handle)
print("\nWyniki BLASTa:")
with open("wyniki_blast.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write("WYNIKI ANALIZY BLAST\n")
    txt_file.write("=" * 30 + "\n")
    for alignment in blast_records.alignments:
        print(f"  Trafienie: {alignment.title}")
        for hsp in alignment.hsps:
            if hsp.expect < 0.01:
                print(f"Identyfikator sekwencji: {alignment.hit_id}")
                print(f"opis sekwencji: {alignment.hit_def}")
                print(f"Poziom dopasowania: {hsp.score}")
                print(f"Istotność statystyczna: {hsp.expect}\n")
                output = (
                    f"Trafienie: {alignment.title}\n"
                    f"Identyfikator sekwencji: {alignment.hit_id}\n"
                    f"Opis sekwencji: {alignment.hit_def}\n"
                    f"Poziom dopasowania (Score): {hsp.score}\n"
                    f"Istotność statystyczna (E-value): {hsp.expect}\n"
                    f"{'-' * 20}\n"
                )
            txt_file.write(output)
            print(f" Zapisano: {alignment.title[:50]}...")
result_handle.close()
print("Analiza zakończona.")



# Drzweo filogenetyczne
print("\nTworzenie wielokrotnego wyrównania sekwencji...")
alignment = MultipleSeqAlignment(fasta_records)
print("Tworzenie drzewa filogenetycznego...")

try:
    calculator = DistanceCalculator('identity')
    dm = calculator.get_distance(alignment)
    constructor = DistanceTreeConstructor(calculator, 'nj')
    tree = constructor.build_tree(alignment)
    fig = plt.figure(figsize=(14, 12), dpi=100)
    ax = fig.add_subplot(1, 1, 1)
    def get_label(clade):
        if clade.is_terminal(): # Jeśli to koniec gałęzi (takson)
            return str(clade.name)
        return "" # Jeśli to węzeł wewnętrzny, zwróć pusty tekst
    Phylo.draw(tree, axes=ax, label_func=get_label, do_show=False)
    plt.ylabel("Taksony", fontsize=12)
    plt.xlabel("Dystans genetyczny", fontsize=12)
    plt.title(f"Drzewo filogenetyczne dla genu {selected_gene}", fontsize=15, pad=20)
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Błąd podczas tworzenia drzewa filogenetycznego: {e}")
       








