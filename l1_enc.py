# create feature to write text file with encoded text and encryption key used
# error handle characters that are not in list
import random
import shutil
from sys import maxsize

# KEY_LOC = r""


class Encoder:
    def __init__(self, char_list):
        self.char_list = char_list
        random.shuffle(self.char_list)

    def encrypt(self, plain_text):
        enc_msg = ''
        shift = random.randint(5, maxsize)
        global key
        key = {" ": " "}

        for i in range(len(self.char_list)):
            key[self.char_list[i]] = self.char_list[(
                i + shift) % len(self.char_list)]

        for i in plain_text:
            if i in key:
                enc_msg += key[i]

        return enc_msg, shift  # returns tuple

    def decrypt(self, encrypted_text):
        dec_msg = ''
        reverse_key = {y: x for (x, y) in key.items()}
        for i in encrypted_text:
            dec_msg += reverse_key[i]

        return dec_msg

# char_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
#             'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
#             '.', ',', '?', '/', '!', '"', ';', ':', '\'', '{', '}', '[',
#             '}', '|', '\\', '$', '%', '@', '*', '-', '_', '+', '=']
# encoder = Encoder(char_set)
# test_msg = encoder.encrypt("hello world")
# print(test_msg)
# print(encoder.decrypt(test_msg))


# Usage
# from l1_enc import Encoder
# file = 'C:/Users/Timothy Chia/Desktop/Projects/Cipher/unicode basic latin.txt'
# char_list = open(file, 'r', encoding='utf-8')
# letters = []

# for i in char_list.read():
#     letters.append(i)

# char_list.close()

# encoder = Encoder(letters)
# msg = input('Enter message: ')
# enc_msg = encoder.encrypt(msg)
# print(f"Encrypted: {enc_msg[0]}")
# print(f"Shift: {enc_msg[1]}")
# print(f"Decrypted: {encoder.decrypt(enc_msg[0])}")
