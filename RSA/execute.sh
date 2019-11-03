#!/usr/bin/env bash

for i in 45 50
do
    echo "Generating keys with $i bits\n" 1>&2
    time python keygen.py $i


    printf "\n\n ENCRYPTING\n" 1>&2
    python crypt.py public_rsa.key text.txt


    printf "\n\n DECRYPTING\n" 1>&2
    python decrypt.py private_rsa.key encrypted.dat


    printf "\n\n DECRYPTING WITH Brute Force\n" 1>&2
    time python bruteforce.py public_rsa.key encrypted.dat


    printf "\n\n DECRYPTING WITH Brute Force + Pollard-Rho\n" 1>&2
    time python pollard-rho.py public_rsa.key encrypted.dat
done