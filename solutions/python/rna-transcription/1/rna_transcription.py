def to_rna(dna_strand):
    DNA = "GCTA"
    RNA = "CGAU"
    translation_table = str.maketrans(DNA, RNA)
    return dna_strand.translate(translation_table)