#The following code will build a simple directory enumeration tool.
#This script takes an approach based on a for loop and passes all "404" responses.

import requests
import sys

#Use wordlist, name wordlist.txt, and put in same folder as this script
sub_list = open("wordlist.txt").read()
directories = sub_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html"
    r = requests.get(dir_enum)
    if r.status_code==404:
        pass
    else:
        print("Valid directory:" ,dir_enum)