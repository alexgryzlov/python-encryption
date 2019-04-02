import caesar_cipher
import vigenere_cipher
import vernam_cipher
import frequencies
import argparse


def do_nothing(string, *args, **kwargs):
    return string


def is_valid_name(name, name_list):
    return name in name_list


def read_from_file(path, *args, action=do_nothing, **kwargs):
    result = ''
    with open(path, 'r') as file:
        for line in file:
            result += line
    return action(result, *args, **kwargs)


def write_to_file(message, path, mode='w'):
    with open(path, mode) as file:
        file.write(message)


cipher_list = {'caesar': caesar_cipher, 'vigenere': vigenere_cipher, 'vernam': vernam_cipher}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    encrypt_parser = subparser.add_parser('encrypt')
    decrypt_parser = subparser.add_parser('decrypt')

    # train subparser creates a character distribution (language model) from a text
    train_parser = subparser.add_parser('train')
    hack_parser = subparser.add_parser('hack')

    train_parser.add_argument('-i', '--input', required=True)
    train_parser.add_argument('--model_file', required=True)

    # if argument is not required it is None by default
    hack_parser.add_argument('-i', '--input')
    hack_parser.add_argument('-o', '--output')
    hack_parser.add_argument('-m', '--model_file', required=True)

    encrypt_parser.add_argument('-i', '--input')
    encrypt_parser.add_argument('-o', '--output')
    encrypt_parser.add_argument('-c', '--cipher', required=True)
    encrypt_parser.add_argument('-k', '--key', required=True)

    decrypt_parser.add_argument('-i', '--input')
    decrypt_parser.add_argument('-o', '--output')
    decrypt_parser.add_argument('-c', '--cipher', required=True)
    decrypt_parser.add_argument('-k', '--key', required=True)
    namespace = parser.parse_args()
    
    if is_valid_name(namespace.cipher, cipher_list):
        cipher = cipher_list[namespace.cipher]
    else:
        raise ValueError("Cipher does not exist or is not supported")

    if namespace.command in ('encrypt', 'decrypt'):
        result = ''
        action_list = {'encrypt': cipher.encode, 'decrypt': cipher.decode}
        action = action_list[namespace.command]
        if namespace.input:
            result = read_from_file(namespace.input, namespace.key, action=action)
        else:
            result = action(input(), namespace.key)
        if namespace.output:
            write_to_file(result, namespace.output)
        else:
            print(result)

    elif namespace.command == 'train':
        message = read_from_file(namespace.input)
        frequency_table = frequencies.make_frequency_table(message)

        for key, value in frequency_table.most_common():
            write_to_file((str(key) + ':' + str(value) + '\n'), namespace.model_file, mode='a')

    elif namespace.command == 'hack':
        frequency_table = frequencies.parse_frequency_table(namespace.model_file)
        if namespace.input:
            encrypted_message = read_from_file(namespace.input)
        else:
            encrypted_message = input()

        best_shift = frequencies.find_best_shift(frequency_table, caesar_cipher.decode, encrypted_message)
        decrypted_message = caesar_cipher.decode(encrypted_message, best_shift)

        if namespace.output:
            write_to_file(decrypted_message, namespace.output)
        else:
            print(decrypted_message)
