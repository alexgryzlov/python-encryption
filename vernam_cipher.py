def encode(message, key):
    encoded_message = []
    for i in range(len(message)):  # len(key) == len(message)
        encoded_message.append(chr(ord(message[i]) ^ ord(key[i])))
    return ''.join(encoded_message)


def decode(message, key):
    decoded_message = []
    for i in range(len(message)):  # len(key) == len(message)
        decoded_message.append(chr(ord(message[i]) ^ ord(key[i])))
    return ''.join(decoded_message)
