#This script will download a file from a website. Useful if you don't have a browser but know where a file is located on the internet.
#Edit the URL section to put in whatever address you want to go to, also modidy line 9 to name the specfic file.
#To run, "python3 filedownload.py

import requests

url = 'https://download.sysinternals.com/files/PSTools.zip'
r = requests.get(url, allow_redirects=True)
open('PSTools.zip', 'wb').write(r.content)
