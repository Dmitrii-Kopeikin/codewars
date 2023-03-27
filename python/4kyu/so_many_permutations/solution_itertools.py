from itertools import permutations as itertools_permutations


def permutations(s):
    return list(''.join(p) for p in set(itertools_permutations(s)))


if __name__ == '__main__':
    pass
