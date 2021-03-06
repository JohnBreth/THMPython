# The script will use a list of potential subdomains and prepends them to the domain name provided via a command-line argument.
# The script then tries to connect to the subdomains and assumes the ones that accept the connection exist.
# Example: python3 subdomenum.py espn.com

import requests
import sys

# Use wordlist, name subdomains.txt, and put in same folder as this script
sub_list = open("subdomains.txt").read()
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domains)

    except requests.ConnectionError:
        pass

    else:
        print("Valid domain: ", sub_domains)
