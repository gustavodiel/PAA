# RSA Algorightm in Python


## Running
To run this Script, just execute in the following order:
```bash
# Generate keys
./keygen.py [NUM OF BITS]

# Encrypt any file
./crypt.py [PUBLIC KEY] [FILE TO ENCRYPT]

# Decrypt the file
./decrypt.py [PRIVATE KEY] [FILE TO DECRYPT]
```


### Running Brute Force
```bash
# Normal Brute Force
./bruteforce.py [PUBLIC KEY] [FILE TO DECRYPT]

# Brute Force with Pollard-Rho
./pollard-rho.py [PUBLIC KEY] [FILE TO DECRYPT]

```