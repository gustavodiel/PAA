#!/usr/bin/python3

import sys


def execute_crypt():
    args = sys.argv

    if len(args) < 3:
        print("Missing args: {} [PUBLIC_KEY] [FILE_TO_ENCRYPT]\nTo generate the key files, run ./keygen\n".format(args[0]))
        exit(-1)

    key_file = args[1]
    source = args[2]

    with open(key_file) as file:
        e = int(file.readline())
        n = int(file.readline())

    with open(source) as file:
        text = file.read()[:-1]

    encrypted = []

    for char in text:
        encrypted.append(pow(ord(char), e, n))

    with open('encrypted.dat', 'w') as file:
        for word in encrypted:
            file.write(str(word))
            file.write('\n')

    print("Dados salvos em encrypted.dat")


if __name__ == '__main__':
    execute_crypt()