from collections import Counter


def find_it(seq):
    counter = Counter(seq)
    for key, value in counter.items():
        if value % 2 != 0:
            return key
    return None
