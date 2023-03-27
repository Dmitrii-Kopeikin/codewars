from collections import Counter


def scramble(s1, s2):
    counter_1 = Counter(s1)
    counter_2 = Counter(s2)

    for key, value in counter_2.items():
        if key in counter_1:
            if counter_2[key] > counter_1[key]:
                return False
        else:
            return False

    return True
