#To run this, download the BeautifulSoup zip file
#http://www.py4e.com/code3/bs4.zip
#or pip install beautifulsoup4 to ensure you have the latest version
#and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup 
import ssl # defauts to certicate verification and most secure protocol (now TLS)

import re

#Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context() 
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE

#try:
url = input('Enter - ') 
html = urllib.request.urlopen(url, context=ctx).read() 
soup = BeautifulSoup(html, 'html.parser')
#if len(url) < 1 : 
    #url = 'https://py4e-data.dr-chuck.net/known_by_Jordanna.html'

try: 
    count = int(input('Enter count:')) 
except: count = 7
try: 
    position = int(input('Enter position:')) 
except: position = 18

while count >= 0 :
# Retrieve all of the anchor tags
    tags = soup('a')
    count = count - 1

    nomes = re.findall(r'known_by_([A-Za-z]+)\.html', url)
    if nomes:
        print(nomes[0])  # Saída: Anayah

    url = (tags[position -1].get('href', None))
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')





