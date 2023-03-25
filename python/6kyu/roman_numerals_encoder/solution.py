def solution(n):
    roman_symbols = [
        ['I', 'V', 'X'],
        ['X', 'L', 'C'],
        ['C', 'D', 'M'],
        ['M', '-', '-']
    ]

    result = ''
    iteration = -1
    while n > 0:
        reminder = n % 10
        n = int(n / 10)
        iteration += 1
        if reminder == 0:
            continue
        elif reminder < 4:
            result += roman_symbols[iteration][0] * reminder
        elif reminder < 5:
            result += roman_symbols[iteration][1] + roman_symbols[iteration][0]
        elif reminder < 9:
            result += roman_symbols[iteration][0] * (reminder - 5) + \
                      roman_symbols[iteration][1]
        else:
            result += roman_symbols[iteration][2] + roman_symbols[iteration][0]

    return result[::-1]
