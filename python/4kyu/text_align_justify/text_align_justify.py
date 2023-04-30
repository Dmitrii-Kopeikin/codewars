def justify(text, width):
    words = text.split()
    lines = []

    start = 0
    end = 0
    line_len = 0
    spaces = 0
    while True:
        if end < len(words) and line_len + spaces + len(words[end]) <= width:
            line_len += len(words[end])
            if line_len + spaces < width:
                spaces += 1
            end += 1
        else:
            if end == len(words):
                lines.append(' '.join(words[start:end]))
                break
            lines.append(create_line(words[start:end], line_len, width))
            line_len = 0
            spaces = 0
            start = end


    return '\n'.join(lines)


def create_line(words: list, length: int, width: int):
    print(words)
    if len(words) <= 1:
        return words[0]
    index = 0
    while length < width:
        words[index] += ' '
        index += 1
        length += 1
        if index == len(words) - 1:
            index = 0

    return ''.join(words)
    

def main():
    print(justify('as ss dd f afsdf asdf asdfa sdfasdf asdfasdfas fasd fas dfasdfasdf adfasd fadsfasf sdfasdfasd', 15))


if __name__ == '__main__':
    main()
