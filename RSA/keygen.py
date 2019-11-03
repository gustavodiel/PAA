#!/usr/bin/python3

import random
import math
import sys


def is_prime(value):
    if value == 2:
        return True

    if value % 2 == 0:
        return False

    if value < 2:
        return False

    for x in range(3, int(value ** 0.5) + 2, 2):
        if value % x == 0:
            return False

    return True


def gen_prime(bits):
    r = 100*(math.log(bits, 2) + 1)  # Tentativas
    r_ = r

    while r > 0:
        n = random.randrange(2 ** (bits - 1), 2 ** bits)
        r -= 1

        if is_prime(n):
            return n

    raise Exception("Failure after" + str(r_ - r) + "tries.")


def mdc(a, b):
    while b != 0:
        a, b = b, a % b

    return a


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


def create_keys():
    if len(sys.argv) < 2:
        print("No bit count found, using 8 bits")
        bit_count = 8
    else:
        bit_count = int(sys.argv[1])

    print("Creating keys with {} bits".format(bit_count))

    # Buscar p e q
    p, q = gen_prime(bit_count), gen_prime(bit_count)

    while p == q:
        q = gen_prime(bit_count)

    # Calculate n
    n = p * q

    # Generate e
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    g = mdc(e, phi)

    while g != 1:
        e = random.randrange(1, phi)
        g = mdc(e, phi)

    # Find d
    d = euclides(e, phi)

    print("Public key: ({}, {})".format(e, n))
    print("Private key: ({}, {})".format(d, n))

    with open('public_rsa.key', 'w') as file:
        file.write(str(e))
        file.write('\n')
        file.write(str(n))
        file.write('\n')

    with open('private_rsa.key', 'w') as file:
        file.write(str(d))
        file.write('\n')
        file.write(str(n))
        file.write('\n')

    print("P: {}\nQ: {}".format(p, q))


if __name__ == '__main__':
    create_keys()
