# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
total = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    #total=0
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('Number:', tag.get('[0-9]+', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    total+= int(tag.contents[0])
    count+= 1
    #print("Count:",tag.count)
    #print("Sum:",sum(int(tag.get('[0-9]+'))))
print("Count",count)
print("Sum",total)