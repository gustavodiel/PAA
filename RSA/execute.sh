#!/usr/bin/env bash

for i in 8 16 32 64 70 80 90 100 110
do
#    echo "Generating keys with $i bits\n" 1>&2
    python keygen.py $i

    python crypt.py public_rsa_$i.key text.txt
#    python decrypt.py private_rsa_$i.key encrypted.dat


    printf "\n\n DECRYPTING WITH Brute Force with $i bits\n" 1>&2
    time python bruteforce.py public_rsa_$i.key encrypted.dat


#    printf "\n\n DECRYPTING WITH Brute Force + Pollard-Rho with $i bits\n" 1>&2
#    time python pollard-rho.py public_rsa_$i.key encrypted.dat


    printf "\n\n ********** \n" 1>&2
done