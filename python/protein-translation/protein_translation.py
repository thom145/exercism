import re


def proteins(strand):

    if len(strand) > 3:
        all_strands = re.findall('...', strand)
        list_strands = list(all_strands)
        for strand in list_strands:


