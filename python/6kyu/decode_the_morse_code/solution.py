from preloaded import MORSE_CODE


def decode_morse(morse_code):
    
    message = ''
    morse_words = morse_code.strip().replace('   ', ' s ').split(' ')
    for word in morse_words:
        if word == 's':
            word = ' '
        else:
            word = MORSE_CODE[word]
        message += word

    return message
