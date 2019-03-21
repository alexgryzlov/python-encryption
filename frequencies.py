import collections
import math

# Create frequency table (character returns its frequency)
def make_frequency_table(message):
    total_chars = 0
    ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    frequency_table = collections.Counter()
    for char in message.lower():
        if char in ru_alphabet:
            frequency_table[char] += 1
            total_chars += 1
    for key in frequency_table:
        frequency_table[key] /= total_chars
    return frequency_table


# Parse frequency table from a file
def parse_frequency_table(path):
    frequency_table = {}
    ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for char in ru_alphabet:
        frequency_table[char] = 0
    file = open(path, 'r')
    for line in file:
        key, value = [i for i in line.split(":")]
        frequency_table[key] = float(value)
    return frequency_table


# Calculate difference between 2 table by summing all squared differences of all characters frequencies
def calculate_frequency_difference(table1, table2):
    difference = 0
    ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for letter in ru_alphabet:
        difference += (table1[letter] - table2[letter]) ** 2
    return difference


def find_best_shift(frequency_table, decrypter, encrypted_message):
    best_value = math.inf
    best_shift = 0
    for shift in range(33):  # 33 - length of Russian alphabet
        decrypted_message = decrypter(encrypted_message, shift)
        current_frequency_table = make_frequency_table(decrypted_message)
        current_value = calculate_frequency_difference(frequency_table, current_frequency_table)
        if current_value < best_value:
            best_value = current_value
            best_shift = shift
    return best_shift
