import urllib.request
import json

url = input('Enter location: ') #http://py4e-data.dr-chuck.net/comments_42.json 
if len(url) < 1 :               #http://py4e-data.dr-chuck.net/comments_2285855.json
    url = 'http://py4e-data.dr-chuck.net/comments_2285855.json'
    
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
comments = info['comments']

names = list()
nums = list()
for item in comments:
  names.append(item['name'])
  nums.append(int(item['count']))

print('Count:',len(names))
print('Sum:',sum(nums))

