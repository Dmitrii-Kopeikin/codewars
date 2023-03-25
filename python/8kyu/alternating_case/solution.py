def to_alternating_case(string: str):
    result = ''
    for c in string:
        if c.isalpha():
            if c.isupper():
                c = c.lower()
            else:
                c = c.upper()
        result += c

    return result
