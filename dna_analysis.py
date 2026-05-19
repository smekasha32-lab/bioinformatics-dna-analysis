
def read_fasta(file_path):
    with open(file_path, 'r') as file:    
        lines = file.readlines()
    
    sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return sequence


def gc_content(dna_sequence):
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    total_length = len(dna_sequence)

    if total_length == 0:
        return 0.0

    return ((g_count + c_count) / total_length) * 100

def find_start_codon(dna_sequence):
    start_codons = ['ATG']
    positions = []
    for i in range(len(dna_sequence) - 2):
        codon = dna_sequence[i:i+3]
        if codon in start_codons:
            positions.append(i)
    return positions

def find_stop_codons(dna_sequence):
    stop_codons = ['TAA', 'TAG', 'TGA']
    positions = []
    for i in range(len(dna_sequence) - 2):
        codon = dna_sequence[i:i+3]
        if codon in stop_codons:
            positions.append(i)
    return positions

def find_orfs(dna_sequence):
    start_positions = find_start_codon(dna_sequence)
    stop_positions = find_stop_codons(dna_sequence)
    orfs = []
    for start in start_positions:
        for stop in stop_positions:
            if stop > start and (stop - start) % 3 == 0:
                orfs.append((start, stop + 3))  # Include the stop codon
                break  
    return orfs

def extract_orf_sequence(file_path):
    orf_sequences = []
    for start, end in find_orfs(read_fasta(file_path)):
        orf_sequence = read_fasta(file_path)[start:end]
        orf_sequences.append(orf_sequence)
    return orf_sequences


codon_table = {
    "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
    "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
    "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
    "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",

    "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
    "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
    "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
    "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",

    "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
    "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
    "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
    "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",

    "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
    "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
    "TAC":"Y", "TAT":"Y", "TAA":"*", "TAG":"*",
    "TGC":"C", "TGT":"C", "TGA":"*", "TGG":"W"
}

def translate_dna_to_protein(dna_sequence):
    protein = ''
    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence [i:i+3]
        amino_acid = codon_table.get(codon, '?')  # '?' for unknown codons
        protein += amino_acid
    return protein

def main():
    file_path = "/Users/sololingz/Desktop/code/career/bioinformatics-dna-analysis/example.fasta"
    seq = read_fasta(file_path)
    print("Sequence :", seq)
    start_positions = find_start_codon(seq)
    stop_positions = find_stop_codons(seq)
    orfs = find_orfs(seq)
    orf_sequences = extract_orf_sequence(file_path)
    start = orfs[0][0] if orfs else None
    end = orfs[0][1] if orfs else None
    for orf in orf_sequences:
        protein = translate_dna_to_protein(orf)
        print("Protein:", protein)

    print("Start codon positions:", start_positions)
    print("Stop codon positions:", stop_positions)
    print("Sequence length:", len(seq))
    print("GC content:", gc_content(seq))
    print("the first 20 bases of the sequence:",seq[:20])
    print("Open reading frames (ORFs):", orfs)
    print("\nORF found:")
    print("Start position:", start)
    print("End position:", end)
    print("Length:", end - start)
    print("Sequence:", orf_sequences)

if __name__ == "__main__":
    main()
    


