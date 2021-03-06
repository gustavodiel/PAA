#!/usr/bin/python3

import sys
import math


def euclides(a, b):
    x = 0
    y = 1
    lx = 1
    ly = 0

    original_b = b

    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)

    if lx < 0:
        lx += original_b

    return lx


def brute_force(n):
    p = int(math.sqrt(n))

    if p % 2 == 0:
        p -= 1

    while n % p != 0 and p < n:
        p += 2

    return p


def find_private_key(e, n):
    p = brute_force(n)

    q = int(n / p)

    phi = (p - 1) * (q - 1)

    # Find d
    d = euclides(e, phi)

    return d


def execute_brute_force():
    args = sys.argv

    if len(args) < 3:
        print("Missing args: {} [PUBLIC_KEY] [FILE_TO_DECRYPT]\nTo generate the key files, run ./keygen\n".format(args[0]))
        exit(-1)

    key_file = args[1]
    source = args[2]

    with open(key_file) as file:
        e = int(file.readline())
        n = int(file.readline())

    d = find_private_key(e, n)

    with open(source) as file:
        text = file.readlines()

    final = []

    for char in text:
        final.append(chr(pow(int(char), d, n)))

    print(''.join(final))


if __name__ == '__main__':
    execute_brute_force()
