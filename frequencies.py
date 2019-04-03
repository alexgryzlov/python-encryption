import collections
import math
from constants import RU_ALPHABET_LOWER as RU_ALPHABET


def make_frequency_table(message):
    """"Create frequency table (character returns its frequency)"""
    total_chars = 0
    frequency_table = collections.Counter()
    for char in message.lower():
        if char in RU_ALPHABET:
            frequency_table[char] += 1
            total_chars += 1
    for key in frequency_table:
        frequency_table[key] /= total_chars
    return frequency_table


def parse_frequency_table(path):
    """"Parse frequency table from a file"""
    frequency_table = {}
    for char in RU_ALPHABET:
        frequency_table[char] = 0
    file = open(path, 'r')
    for line in file:
        key, value = [i for i in line.split(":")]
        frequency_table[key] = float(value)
    return frequency_table


def calculate_frequency_difference(table1, table2):
    """"Calculate difference between 2 table by summing all squared differences of all characters frequencies"""
    difference = 0
    for letter in RU_ALPHABET:
        difference += (table1[letter] - table2[letter]) ** 2
    return difference


def find_best_shift(frequency_table, decrypter, encrypted_message):
    best_value = math.inf
    best_shift = 0
    for shift in range(len(RU_ALPHABET)):
        decrypted_message = decrypter(encrypted_message, shift)
        current_frequency_table = make_frequency_table(decrypted_message)
        current_value = calculate_frequency_difference(frequency_table, current_frequency_table)
        if current_value < best_value:
            best_value = current_value
            best_shift = shift
    return best_shift
