import re

from preloaded import MORSE_CODE


def decode_bits(bits: str):
    bits = bits.strip('0')
    signals = set(re.findall(r'0+|1+', bits))
    rate = len(min(signals, key=len))

    return bits[::rate].replace('111', '-') \
        .replace('0000000', '   ') \
        .replace('000', ' ') \
        .replace('1', '.') \
        .replace('0', '')


def decode_morse(morse_code):
    message = ''
    morse_words = morse_code.strip().replace('   ', ' s ').split(' ')
    for word in morse_words:
        message += MORSE_CODE[word] if word != 's' else ' '

    return message
