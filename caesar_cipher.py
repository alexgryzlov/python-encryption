def encode(message, shift=1):
    shift = int(shift)
    shift %= 33
    ru_alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    ru_alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabets = [ru_alphabet_upper, ru_alphabet_lower]
    encoded_message = []
    for char in message:
        alphabet = ''
        for current_alphabet in alphabets:
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
    shift %= 33
    ru_alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    ru_alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabets = [ru_alphabet_upper, ru_alphabet_lower]
    decoded_message = []
    for coded_char in encoded_message:
        alphabet = ''
        for current_alphabet in alphabets:
            if coded_char in current_alphabet:
                alphabet = current_alphabet
        if alphabet == '':
            decoded_message.append(coded_char)
            continue
        decoded_char = alphabet[(alphabet.index(coded_char) - shift) % len(alphabet)]
        decoded_message.append(decoded_char)
    return ''.join(decoded_message)
