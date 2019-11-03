#!/usr/bin/python3

import sys


def execute_decrypt():
    args = sys.argv

    if len(args) < 3:
        print("Missing args: {} [PRIVATE_KEY] [FILE_TO_DECRYPT]\n".format(args[0]))
        exit(-1)

    key_file = args[1]
    source = args[2]

    with open(key_file) as file:
        d = int(file.readline())
        n = int(file.readline())

    with open(source) as file:
        text = file.readlines()

    final = []

    for char in text:
        final.append(chr(pow(int(char), d, n)))

    print(''.join(final))


if __name__ == '__main__':
    execute_decrypt()
