import xml.etree.ElementTree as ET
import re

data = """ 
    <person>
        <name>Chuck</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person> """

tree = ET.fromstring(data)
""" print("Name:", tree.find('name').text)
print("Name Attr:", tree.find('email').get('hide'))
print("Phone:", tree.find('phone').text)
print("Phone Attr:", tree.find('phone').get('type')) """

# Often the XML has multiple nodes and we need to write a loop to process all of the nodes. In the following program, we 
# loop through all of the user nodes:
inputs = '''
    <stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>
    </stuff> '''

users_stuff = ET.fromstring(inputs)
lst = users_stuff.findall('users/user')
""" print("User count:", len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute:', item.get('x'))
    print('\r') """

import json

data = """ 
    [
        {"id": "001",
         "x": "2",
         "name": "Chuck"
        },
        {"id": "009",
         "x": "7",
         "name": "Brent"
        }
    ] """

info = json.loads(data)
""" print("User count:", len(info))

for item in info:
    print("Name:", item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x'])
    print('\r') """

# 13.9 APPLICATION 1: GOOGLE GEOCODING WEB SERVICE
import urllib.request, urllib.parse, urllib.error
import ssl

""" api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

# my_api_key_1 = "keyString":"AIzaSyBp7Q1VXFdBMaFccwdxcRXgoPk5xbI0p0Y"
# my_api_key_2 = "keyString":"AIzaSyCeTEIdsnl5Z2tI2IQahUiXtWzCDePmYkg"

# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ").strip()
    if len(address) < 1: break
    
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms) 
    
    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None
        
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    print(json.dumps(js, indent=4))
    
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location) """

# You can download www.py4e.com/code3/geoxml.py to explore the XML variant of the Google geocoding API.

""" api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'
    
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ').strip()
    if len(address) < 1: break
    
    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)
    
    try:
        results = tree.findall('result')
    except:
        results = None
    
    print(data.decode())
    
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text
    
    print('lat:', lat, 'lng:', lng)
    print(location) """

# Exercise 1: Change either geojson.py or geoxml.py to print out the two character country code from the retrieved data. 
# Add error checking so your program does not traceback if the country code is not there. Once you have it working, 
# search for “Atlantic Ocean” and make sure it can handle locations that are not in any country.

""" api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

# my_api_key_1 = "keyString":"AIzaSyBp7Q1VXFdBMaFccwdxcRXgoPk5xbI0p0Y"
# my_api_key_2 = "keyString":"AIzaSyCeTEIdsnl5Z2tI2IQahUiXtWzCDePmYkg"

# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    try:
        while True:
            address = input("Enter location (Country): ").strip()
            if len(address) < 1: break
            
            parms = dict()
            parms['address'] = address
            if api_key is not False: parms['key'] = api_key
            url = serviceurl + urllib.parse.urlencode(parms) 
            
            print("Retrieving", url)
            uh = urllib.request.urlopen(url, context=ctx)
            data = uh.read().decode()
            print('Retrieved', len(data), 'characters')
            
            try:
                js = json.loads(data)
            except:
                js = None
                
            if not js or 'status' not in js or js['status'] != 'OK':
                print('==== Failure To Retrieve ====')
                print(data)
                continue
            
            print(json.dumps(js, indent=4))
            
            lat = js['results'][0]['geometry']['location']['lat']
            lng = js['results'][0]['geometry']['location']['lng']
            country_code = js['results'][0]['address_components'][0]['short_name']
            print('Country Code:', country_code)
            print('lat', lat, 'lng', lng)
            location = js['results'][0]['formatted_address']
            print(location)
    except:
        print(f'Please enter a valid location not "{address}"')
        continue
    break """
    
# 13.10 APPLICATION 2: TWITTER    
# The Twitter web service are accessed using a URL like this:
# https://api.twitter.com/1.1/statuses/user_timeline.json

# My_Bearer_Token = 'AAAAAAAAAAAAAAAAAAAAAMG3rQEAAAAAHzc7zvS%2BN6JOskq66k1cH%2FHkh5M%3DD76xcuelUDhXKifb4KtBi6iy5esYtqHFSzCIBjKfgb09slcUZi'

# My_API_Key = 'dZxbWYFRCz19cDr1T3VeYiSZq'
# My_API_Key_Secret = 'HM1nsdKXKZ72odvJsNpfZlnZrC0jRtFDMPIh2953kZeipuLHEf'
# My_Access_Token = '1114569589671776256-mV7kEug8YAb4wqxmqPLFbltccLVTEQ'
# My_Access_Token_Secret = 'xVfPH3v8E8S7rBTLUK5usbHgCAjn9WIvod5vMRi6AWpIY'

# Here is your OAuth 2.0 Client ID and Client Secret
# Client ID = 'aGtpbHphS3ZHWlZOZ01jdmFHOFI6MTpjaQ'
# Client Secret = 'ZKWNF93ZX8pUsbkGkVU_0OKepH_tkPTkvf9KaSgZiH3RQiCk9t'

# Chapter-13-Using-Web-Services.py   
    






















