from itertools import product

DIGIT_VARIATIONS = [
    ['0', '8'],
    ['1', '2', '4'],
    ['1', '2', '3', '5'],
    ['2', '3', '6'],
    ['1', '4', '5', '7'],
    ['2', '4', '5', '6', '8'],
    ['3', '5', '6', '9'],
    ['4', '7', '8'],
    ['5', '7', '8', '9', '0'],
    ['6', '8', '9']
]


def get_pins(observed):
    if not observed:
        return []

    return [''.join(p) for p in product(*(DIGIT_VARIATIONS[int(d)] for d in observed))]


def main():
    print(get_pins('12'))

if __name__ == '__main__':
    main()