def encode(message, key):
    if len(key) != len(message):
        raise ValueError("Key's length doesn't match message's length")
    encoded_message = []
    for i in range(len(message)):
        encoded_message.append(chr(ord(message[i]) ^ ord(key[i])))
    return ''.join(encoded_message)


def decode(message, key):
    if len(key) != len(message):
        raise ValueError("Key's length doesn't match message's length")
    decoded_message = []
    for i in range(len(message)):  # len(key) == len(message)
        decoded_message.append(chr(ord(message[i]) ^ ord(key[i])))
    return ''.join(decoded_message)
