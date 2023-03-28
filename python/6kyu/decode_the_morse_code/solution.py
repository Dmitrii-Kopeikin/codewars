from preloaded import MORSE_CODE


def decode_morse(morse_code):

    message = ''
    morse_words = morse_code.strip().replace('   ', ' s ').split(' ')
    for word in morse_words:
        message += MORSE_CODE[word] if word != 's' else ' '

    return message
