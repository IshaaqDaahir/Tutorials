import socket
""" mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close() """

# The next example uses b'' notation to specify that a variable should be stored as a bytes object. encode() and b'' are 
# equivalent.
b_bytes = b"Hello world!"
# print(b_bytes)
# print(b_bytes.decode())

normal_encoding = 'Hello world!'.encode()
# print(normal_encoding.decode())

import time

""" HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')

count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data
     
mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n") 
print("Header length", pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close() """

# Once the web page has been opened with urllib.request.urlopen, we can treat it like a file and read through it using a 
# for loop.
""" import urllib.request

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip()) """

# As an example, we can write a program to retrieve the data for romeo.txt and compute the frequency of each word in the 
# file as follows:
import urllib.request, urllib.parse, urllib.error

""" fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts) """

# Sometimes you want to retrieve a non-text (or binary) file such as an image or video file. The data in these files is 
# generally not useful to print out, but you can easily make a copy of a URL to a local file on your hard disk using 
# urllib.
""" img = urllib.request.urlopen("http://data.pr4e.org/cover3.jpg").read()
fhand = open("cover3.jpg", "wb")
fhand.write(img)
fhand.close() """

# However if this is a large audio or video file, this program may crash or at least run extremely slowly when your 
# computer runs out of memory. In order to avoid running out of memory, we retrieve the data in blocks (or buffers) and 
# then write each block to your disk before retrieving the next block.
""" img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)
    
print(size, 'characters copied.')
fhand.close() """

# One simple way to parse HTML is to use regular expressions to repeatedly search for and extract substrings that match a 
# particular pattern.

# Search for link values within URL input
import re 
import ssl

# Ignore SSL certificate errors
""" ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL here: ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode()) """

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
""" ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
# tags = soup("img")
tags = soup("a")
for tag in tags:
    # print(tag.get('src', None))
    print(tag.get('href', None)) """
    
from urllib.request import urlopen

# Ignore SSL certificate errors
""" ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'lxml')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print("URL:", tag.get('href', None))
    # print("Contents:", tag.contents[0])
    print("Contents:", tag.contents)
    print("Attributes:", tag.attrs)
    
# URL for testing this loop
# http://www.dr-chuck.com/page1.htm """

# There is also a curl3.py sample program that does this task a little more effectively, in case you actually want to use 
# this pattern in a program you are writing.
import os

""" print("Please enter a URL like http://data.pr4e.org/cover3.jpg")
urlstr = input().strip()
img = urllib.request.urlopen(urlstr)

# Get the last "word"
words = urlstr.split('/')
fname = words[-1]

# Don't ovewrite the file
if os.path.exists(fname):
    if input('Replace ' + fname + ' (Y/n)?: ') != 'Y':
        print('Data not copied')
        exit()
    print('Replacing', fname)

fhand = open(fname, 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)
    
print(size, 'characters copied to', fname)
fhand.close() """

# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. You can use split('/') 
# to break the URL into its component parts so you can extract the host name for the socket connect call. Add error 
# checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.
""" while True:
    try:
        urlstr = input('Enter URL: ')
        urlstr_words = urlstr.split('/')
        HOST = urlstr_words[2]

        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((HOST, 80))
        cmd = f"GET {urlstr} HTTP/1.0\r\n\r\n".encode()
        mysock.send(cmd)

        while True:
            data = mysock.recv(512)
            if len(data) < 1: break
            print(data.decode())
            
        mysock.close()
        break
    except:
        print(f'Please enter a valid URL not "{urlstr}"')
        continue """

# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying 
# any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number 
# of characters and display the count of the number of characters at the end of the document.        
""" while True:
    try:
        urlstr = input('Enter URL: ')
        urlstr_words = urlstr.split('/')
        HOST = urlstr_words[2]

        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((HOST, 80))
        cmd = f"GET {urlstr} HTTP/1.0\r\n\r\n".encode()
        mysock.send(cmd)

        decoded_data_list = []
        count = 0
        while True:
            data = mysock.recv(512)
            decoded_data = data.decode()
            count = count + len(decoded_data)
            if len(data) < 1: break
            for char in decoded_data:
                decoded_data_list.append(char)
                
        print(decoded_data_list[:3000])
        print(f"Total characters received: {count}")

        mysock.close()
        break
    except:
        print(f'Please enter a valid URL not "{urlstr}"')
        continue """
        
# Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 
# characters, and (3) counting the overall number of characters in the document. Don’t worry about the headers for this 
# exercise, simply show the first 3000 characters of the document contents.
# Ignore SSL certificate errors
import string
""" while True:
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url = input('Enter URL here: ')
        data = urllib.request.urlopen(url, context=ctx)

        decoded_data_list = []
        count = 0
        while True:
            decoded_data = data.read(100000).decode()
            # decoded_data = decoded_data.translate(str.maketrans('', '', string.punctuation))
            count = count + len(decoded_data)
            if len(decoded_data) < 1: break
            for char in decoded_data:
                decoded_data_list.append(char)
            
        print(decoded_data_list[:30])
        print(f"Total characters received: {count}")
        break
    
    except:        
        print(f'Please enter a valid URL not "{url}"')
        continue """

# Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document and display the 
# count of the paragraphs as the output of your program. Do not display the paragraph text, only count them. Test your 
# program on several small web pages as well as some larger web pages.

# Ignore SSL certificate errors
""" ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'lxml')

# Retrieve all of the paragraph tags
tags = soup("p")

count = 0
for tag in tags:
    count += 1
print(f'The total number of paragraphs is: "{count}"') """
# URL for testing this loop
# http://www.dr-chuck.com/page1.htm
# https://www.ebay.com/help/buying/paying-items/buying-guest?id=4035&st=7

# Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have 
# been received. Remember that recv receives characters (newlines and all), not lines.
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
mysock.sendall(b'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n')

contents = b''
while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    contents = contents + data
    newline_pos = contents.find(b"\r\n\r\n")
    
print(contents[newline_pos+4:-1].decode())
mysock.close()


































































































































































































































































































































































































































































