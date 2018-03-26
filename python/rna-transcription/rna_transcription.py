def to_rna(dna_strand):
    rna_dict = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    try:
        rna_strand = [rna_dict[nucleotide]
                      for nucleotide in dna_strand.upper()]
    except:
        raise ValueError("you have entered a string that isn\'t a dna strand")
    return ''.join(rna_strand)
