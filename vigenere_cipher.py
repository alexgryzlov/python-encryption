from constants import ALPHABETS


def encode(message, key="СОРОКДВА"):
    encoded_message = []
    i = 0
    for char in message:
        alphabet = ''
        for current_alphabet in ALPHABETS:
            if char in current_alphabet:
                alphabet = current_alphabet
        if alphabet == '':
            encoded_message.append(char)
            i = (i + 1) % len(key)
            continue
        encoded_char = alphabet[(alphabet.lower().index(key.lower()[i]) + alphabet.index(char)) % len(alphabet)]
        i = (i + 1) % len(key)
        encoded_message.append(encoded_char)
    return ''.join(encoded_message)


def decode(message, key="СОРОКДВА"):
    decoded_message = []
    i = 0
    for encoded_char in message:
        alphabet = ''
        for current_alphabet in ALPHABETS:
            if encoded_char in current_alphabet:
                alphabet = current_alphabet
        if alphabet == '':
            decoded_message.append(encoded_char)
            i = (i + 1) % len(key)
            continue
        decoded_char = alphabet[(alphabet.index(encoded_char) - alphabet.lower().index(key.lower()[i])) % len(alphabet)]
        i = (i + 1) % len(key)
        decoded_message.append(decoded_char)
    return ''.join(decoded_message)
