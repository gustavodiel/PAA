#!/usr/bin/env bash

#for k in 1 2 3 4 5 6 7 8 9
#do
#    printf "\n\n TEST $k\n" 1>&2
#    for i in 100 500 1000 1500 2000 2500 3000 3500 4000 4500
#    do
#        echo "Generating keys with $i bits\n" 1>&2
#        time python keygen.py $i
#
#        printf "\n\n ********** \n" 1>&2
#    done
#done
#
#for k in 1 2 3 4 5 6 7 8 9
#do
#    printf "\n\n TEST $k\n" 1>&2
#    for i in 10 20 30 40 50 60 70
#    do
##        echo "Generating keys with $i bits\n" 1>&2
#        python keygen.py $i
#
#        python crypt.py public_rsa_$i.key text.txt
#    #    python decrypt.py private_rsa_$i.key encrypted.dat
#
#
#        printf "\n\n DECRYPTING WITH Brute Force with $i bits\n" 1>&2
#        time python bruteforce.py public_rsa_$i.key encrypted.dat
#
#
#        printf "\n\n ********** \n" 1>&2
#    done
#done

for k in 1 2 3 4 5 6 7 8 9
do
    printf "\n\n TEST $k\n" 1>&2
    for i in 10 20 30 40 50 60 70 80 90 100 110
    do
#        echo "Generating keys with $i bits\n" 1>&2
        python keygen.py $i

        python crypt.py public_rsa_$i.key text.txt
    #    python decrypt.py private_rsa_$i.key encrypted.dat

        printf "\n\n DECRYPTING WITH Brute Force + Pollard-Rho with $i bits\n" 1>&2
        time python pollard-rho.py public_rsa_$i.key encrypted.dat

        printf "\n\n ********** \n" 1>&2
    done
done