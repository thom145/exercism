def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        return sum([1 for countA in range(len(strand_a)) if strand_a[countA] != strand_b[countA]])

    else:
        raise ValueError("Strands aren't of the same length")
