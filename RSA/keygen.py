#!/usr/bin/python3

import random
import math
import sys


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False

        i = i + 6

    return True


def is_probably_prime(n, k=5):
    if n < 2:
        return False

    for i in range(0, k):
        a = random.randint(1, n-1)
        if pow(a, n-1, n) != 1:
            return False

    return True


def gen_prime(bits):
    inf_limit = pow(2, (bits - 1))
    sup_limit = pow(2, bits)

    while True:
        n = random.randrange(inf_limit, sup_limit)

        if is_probably_prime(n):
            return n


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

    if bit_count < 8:
        print("Minimum bit count is 8!")
        bit_count = 8

    print("Creating keys with {} bits".format(bit_count))

    half_bit_count = int(bit_count / 2)

    # Buscar p e q
    p, q = gen_prime(half_bit_count), gen_prime(half_bit_count)

    while p == q:
        q = gen_prime(half_bit_count)

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

    with open("public_rsa_{}.key".format(bit_count), 'w') as file:
        file.write(str(e))
        file.write('\n')
        file.write(str(n))
        file.write('\n')

    with open("private_rsa_{}.key".format(bit_count), 'w') as file:
        file.write(str(d))
        file.write('\n')
        file.write(str(n))
        file.write('\n')

    print("P: {}\nQ: {}".format(p, q))


if __name__ == '__main__':
    create_keys()
