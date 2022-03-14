#This script is used to crack a hash given a password list and an identified hash value.
#To see ascii art you need to also run "apt install python3-pyfiglet" prior to running script, if not comment out line 9-10.
#You can modify the type of hash by editing line 17, for example "hashlib.md5" can become "hashlib.sha256".
#To run script, type "python3 hashcrack.py", then when prompted enter the worldlist location and hash to be cracked.

import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("TryHackMe \n Python 4 Pentesters \n HASH CRACKER for MD 5")
print(ascii_banner)

wordlist_location = str(input('Enter wordlist file location: '))
hash_input = str(input('Enter hash to be cracked: '))

with open(wordlist_location, 'r') as file:
    for line in file.readlines():
        hash_ob = hashlib.md5(line.strip().encode())
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == hash_input:
            print('Found cleartext password! ' + line.strip())
            exit(0)