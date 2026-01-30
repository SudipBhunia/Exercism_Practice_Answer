codon_to_amino_acid = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}
def proteins(strand):
    res = []
    for i in range(0,len(strand), 3):
        if strand[i:i+3] in codon_to_amino_acid:
            if codon_to_amino_acid[strand[i:i+3]] != "STOP":
                res.append(codon_to_amino_acid[strand[i:i+3]])
            else:
                break
    return res