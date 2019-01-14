def to_rna(dna_strand):
    """
    Return the rna value of a dna strand input
    returns the rna value as a string
    """
    rta = [] # create an empty rna  string
    dna = list(dna_strand) # create a list of dna so iterating is possible
    to_replace = {'C': 'G', 'G': 'C', 'T': 'A', 'A': 'U'}
    for letter in dna:
        if letter in to_replace.keys():
            rta.append(to_replace[letter])
    return ''.join(rta) # returning the rta string

print(to_rna('ACGTGGTCTTAA'))

