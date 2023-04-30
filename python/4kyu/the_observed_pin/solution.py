def get_pins(observed):
    if not observed:
        return []

    digit_variations = [
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
    pin_variations = ['']

    for digit_c in observed:
        digit = int(digit_c)
        pin_variations *= len(digit_variations[digit])
        for i in range(0, len(pin_variations)):
            j = i // (len(pin_variations) // len(digit_variations[digit]))
            pin_variations[i] += digit_variations[digit][j]

    return pin_variations        
