import random


# This table tells Python how to translate DNA codons into amino acids.
# A codon is a group of 3 DNA letters.
CODON_TABLE = {
    "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
    "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
    "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
    "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",

    "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
    "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",

    "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
    "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
    "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
    "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",

    "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
    "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
    "TAC": "Y", "TAT": "Y", "TAA": "*", "TAG": "*",
    "TGC": "C", "TGT": "C", "TGA": "*", "TGG": "W",
}

import random


# This table tells Python how to translate DNA codons into amino acids.
# A codon is a group of 3 DNA letters.
CODON_TABLE = {
    "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
    "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
    "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
    "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",

    "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
    "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",

    "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
    "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
    "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
    "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",

    "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
    "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
    "TAC": "Y", "TAT": "Y", "TAA": "*", "TAG": "*",
    "TGC": "C", "TGT": "C", "TGA": "*", "TGG": "W",
}


def read_fasta(file_path):
    """Read a FASTA file and return only the DNA sequence."""
    with open(file_path, "r") as file:
    """Read a FASTA file and return only the DNA sequence."""
    with open(file_path, "r") as file:
        lines = file.readlines()

    dna_sequence = ""

    for line in lines:
        line = line.strip()

        # FASTA header lines start with >, so we skip them.
        if not line.startswith(">"):
            dna_sequence = dna_sequence + line

    return dna_sequence.upper()

    dna_sequence = ""

    for line in lines:
        line = line.strip()

        # FASTA header lines start with >, so we skip them.
        if not line.startswith(">"):
            dna_sequence = dna_sequence + line

    return dna_sequence.upper()


def gc_content(dna_sequence):
    """Calculate how much of the DNA is G or C."""
    g_count = dna_sequence.count("G")
    c_count = dna_sequence.count("C")
    """Calculate how much of the DNA is G or C."""
    g_count = dna_sequence.count("G")
    c_count = dna_sequence.count("C")
    total_length = len(dna_sequence)

    if total_length == 0:
        return 0

    gc_percent = ((g_count + c_count) / total_length) * 100
    return gc_percent
        return 0

    gc_percent = ((g_count + c_count) / total_length) * 100
    return gc_percent


def find_start_codons(dna_sequence):
    """Find every place where the start codon ATG appears."""
def find_start_codons(dna_sequence):
    """Find every place where the start codon ATG appears."""
    positions = []


    for i in range(len(dna_sequence) - 2):
        codon = dna_sequence[i:i + 3]

        if codon == "ATG":
        codon = dna_sequence[i:i + 3]

        if codon == "ATG":
            positions.append(i)


    return positions



def find_stop_codons(dna_sequence):
    """Find every place where a stop codon appears."""
    stop_codons = ["TAA", "TAG", "TGA"]
    """Find every place where a stop codon appears."""
    stop_codons = ["TAA", "TAG", "TGA"]
    positions = []


    for i in range(len(dna_sequence) - 2):
        codon = dna_sequence[i:i + 3]

        codon = dna_sequence[i:i + 3]

        if codon in stop_codons:
            positions.append(i)


    return positions



def find_orfs(dna_sequence):
    """Find ORFs.

    ORF means open reading frame.
    In this beginner version:
    - it starts with ATG
    - it ends with TAA, TAG, or TGA
    - the stop codon must be in the same reading frame
    """
    start_positions = find_start_codons(dna_sequence)
    """Find ORFs.

    ORF means open reading frame.
    In this beginner version:
    - it starts with ATG
    - it ends with TAA, TAG, or TGA
    - the stop codon must be in the same reading frame
    """
    start_positions = find_start_codons(dna_sequence)
    stop_positions = find_stop_codons(dna_sequence)
    orfs = []


    for start in start_positions:
        for stop in stop_positions:
            same_reading_frame = (stop - start) % 3 == 0

            if stop > start and same_reading_frame:
                # stop + 3 includes the stop codon in the ORF sequence.
                orfs.append((start, stop + 3))
                break

            same_reading_frame = (stop - start) % 3 == 0

            if stop > start and same_reading_frame:
                # stop + 3 includes the stop codon in the ORF sequence.
                orfs.append((start, stop + 3))
                break

    return orfs


def extract_orf_sequences(dna_sequence):
    """Use ORF positions to pull out the actual ORF DNA sequences."""
    orfs = find_orfs(dna_sequence)

def extract_orf_sequences(dna_sequence):
    """Use ORF positions to pull out the actual ORF DNA sequences."""
    orfs = find_orfs(dna_sequence)
    orf_sequences = []

    for start, end in orfs:
        orf_sequence = dna_sequence[start:end]

    for start, end in orfs:
        orf_sequence = dna_sequence[start:end]
        orf_sequences.append(orf_sequence)


    return orf_sequences


def translate_dna_to_protein(dna_sequence):
    """Translate DNA into a protein sequence."""
    protein = ""

    # Move through DNA 3 letters at a time.
    """Translate DNA into a protein sequence."""
    protein = ""

    # Move through DNA 3 letters at a time.
    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i + 3]
        amino_acid = CODON_TABLE.get(codon, "?")
        protein = protein + amino_acid

        codon = dna_sequence[i:i + 3]
        amino_acid = CODON_TABLE.get(codon, "?")
        protein = protein + amino_acid

    return protein


def mutate_one_base(dna_sequence):
    """Change one random DNA base into a different base."""
    bases = ["A", "T", "C", "G"]
    dna_list = list(dna_sequence)

    position = random.randint(0, len(dna_list) - 1)
    old_base = dna_list[position]

    possible_new_bases = []
    for base in bases:
        if base != old_base:
            possible_new_bases.append(base)

    new_base = random.choice(possible_new_bases)
    dna_list[position] = new_base

    mutated_sequence = "".join(dna_list)

    print("Mutation:")
    print("Position:", position)
    print("Old base:", old_base)
    print("New base:", new_base)

    return mutated_sequence



def mutate_one_base(dna_sequence):
    """Change one random DNA base into a different base."""
    bases = ["A", "T", "C", "G"]
    dna_list = list(dna_sequence)

    position = random.randint(0, len(dna_list) - 1)
    old_base = dna_list[position]

    possible_new_bases = []
    for base in bases:
        if base != old_base:
            possible_new_bases.append(base)

    new_base = random.choice(possible_new_bases)
    dna_list[position] = new_base

    mutated_sequence = "".join(dna_list)

    print("Mutation:")
    print("Position:", position)
    print("Old base:", old_base)
    print("New base:", new_base)

    return mutated_sequence


def main():
    file_path = "example.fasta"
    dna_sequence = read_fasta(file_path)

    print("DNA sequence:", dna_sequence)
    print("Sequence length:", len(dna_sequence))
    print("First 20 bases:", dna_sequence[:20])
    print("GC content:", gc_content(dna_sequence), "%")
    print()

    start_positions = find_start_codons(dna_sequence)
    stop_positions = find_stop_codons(dna_sequence)
    orfs = find_orfs(dna_sequence)
    orf_sequences = extract_orf_sequences(dna_sequence)
    file_path = "example.fasta"
    dna_sequence = read_fasta(file_path)

    print("DNA sequence:", dna_sequence)
    print("Sequence length:", len(dna_sequence))
    print("First 20 bases:", dna_sequence[:20])
    print("GC content:", gc_content(dna_sequence), "%")
    print()

    start_positions = find_start_codons(dna_sequence)
    stop_positions = find_stop_codons(dna_sequence)
    orfs = find_orfs(dna_sequence)
    orf_sequences = extract_orf_sequences(dna_sequence)

    print("Start codon positions:", start_positions)
    print("Stop codon positions:", stop_positions)
    print("ORF positions:", orfs)
    print("ORF sequences:", orf_sequences)
    print()

    for orf_sequence in orf_sequences:
        protein = translate_dna_to_protein(orf_sequence)
        print("ORF DNA:", orf_sequence)
        print("Protein:", protein)
        print()

    mutated_sequence = mutate_one_base(dna_sequence)
    print("Original DNA:", dna_sequence)
    print("Mutated DNA: ", mutated_sequence)

    print("ORF positions:", orfs)
    print("ORF sequences:", orf_sequences)
    print()

    for orf_sequence in orf_sequences:
        protein = translate_dna_to_protein(orf_sequence)
        print("ORF DNA:", orf_sequence)
        print("Protein:", protein)
        print()

    mutated_sequence = mutate_one_base(dna_sequence)
    print("Original DNA:", dna_sequence)
    print("Mutated DNA: ", mutated_sequence)


if __name__ == "__main__":
    main()
