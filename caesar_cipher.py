from constants import ALPHABETS
from constants import RU_ALPHABET_LOWER as RU_ALPHABET


def encode(message, shift=1):
    shift = int(shift)
    shift %= len(RU_ALPHABET)
    encoded_message = []
    for char in message:
        alphabet = ''
        for current_alphabet in ALPHABETS:
            if char in current_alphabet:
                alphabet = current_alphabet
        if alphabet == '':
            encoded_message.append(char)
            continue
        encoded_char = alphabet[(alphabet.index(char) + shift) % len(alphabet)]
        encoded_message.append(encoded_char)
    return ''.join(encoded_message)


def decode(encoded_message, shift=1):
    shift = int(shift)
    shift %= len(RU_ALPHABET)
    decoded_message = []
    for coded_char in encoded_message:
        alphabet = ''
        for current_alphabet in ALPHABETS:
            if coded_char in current_alphabet:
                alphabet = current_alphabet
        if alphabet == '':
            decoded_message.append(coded_char)
            continue
        decoded_char = alphabet[(alphabet.index(coded_char) - shift) % len(alphabet)]
        decoded_message.append(decoded_char)
    return ''.join(decoded_message)
