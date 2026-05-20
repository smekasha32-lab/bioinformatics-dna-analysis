# Bioinformatics DNA Analysis

This is a beginner Python project for analyzing a DNA sequence.

Everything is in one file for now:

- `dna_analysis.py`

The example DNA sequence is in:

- `example.fasta`

## What the Code Does

The script can:

- read a FASTA file
- calculate GC content
- find start codons
- find stop codons
- find ORFs
- translate DNA into protein

## Run It

```bash
python3 dna_analysis.py
```

## Biology Words

FASTA: a common file format for DNA sequences.

GC content: the percent of the sequence made of G and C bases.

Codon: a group of 3 DNA bases.

Start codon: usually `ATG`.

Stop codons: `TAA`, `TAG`, and `TGA`.

ORF: open reading frame. In this project, it starts with `ATG` and ends with a
stop codon in the same reading frame.

Protein translation: changing DNA codons into amino acid letters.

## Technologies Used

- Python 3
- VS Code
- Git
- GitHub

## Technologies Used

- Python 3
- VS Code
- Git
- GitHub

---

## Output

Protein: MRYACSRSIDR*
