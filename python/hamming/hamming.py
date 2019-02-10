def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        if strand_a == strand_b:
            return 0
        else:
            count = 0
            for countA in range(len(strand_a)):
                if strand_a[countA] != strand_b[countA]:
                    count += 1
            return count
    else:
        raise ValueError("Strands aren't of the same length")