import re

protein_dict = {'Methionine': ['AUG'],
                'Phenylalanine': ['UUU', 'UUC'],
                'Leucine': ['UUA', 'UUG'],
                'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
                'Tyrosine': ['UAU', 'UAC'],
                'Cysteine': ['UGU', 'UGC'],
                'Tryptophan': ['UGG'],
                'STOP': ['UAA', 'UAG', 'UGA']
                }

def proteins(strand):
    if str(type(strand)) == "<class 'list'>": # given strand is already a list
        return lookUpStrand(strand)
    else:                                     # create a list from the given strand
        if len(strand) > 3:                   # if more than one strand separate them
            all_strands = list(re.findall('...', strand))
            return lookUpStrand(all_strands)
        else:
            return lookUpStrand([strand])


def lookUpStrand(strandsList):
    protein = []
    for strand in strandsList:
        for key, values in protein_dict.items():
            for value in values:
                if value == strand:
                    if key == 'STOP':
                        return protein
                    else:
                        protein.append(key)
    return protein