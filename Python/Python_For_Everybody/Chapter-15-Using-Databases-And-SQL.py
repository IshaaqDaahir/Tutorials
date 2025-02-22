import sqlite3

# The first SQL command removes the Tracks table from the database if it exists. This pattern is simply to allow us to 
# run the same program to create the Tracks table over and over again without causing an error. Note that the DROP 
# TABLE command deletes the table and all of its contents from the database (i.e., there is no “undo”).
""" conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks(title TEXT, plays INTEGER)')

conn.close() """

""" # Now that we have created a table named Tracks, we can put some data into that table using the SQL INSERT operation. 
# Again, we begin by making a connection to the database and obtaining the cursor. We can then execute SQL commands 
# using the cursor.
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute("INSERT INTO Tracks (title, plays) VALUES(?, ?)", ("Thunderstruck", 20))
cur.execute("INSERT INTO Tracks (title, plays) VALUES(?, ?)", ("My Way", 15))
conn.commit()

print("Tracks:")
# cur.execute("SELECT title, plays FROM Tracks")
# cur.execute("SELECT * FROM Tracks WHERE title = 'My Way'")
# cur.execute("SELECT title, plays FROM Tracks ORDER BY title")
cur.execute("SELECT title, plays FROM Tracks ORDER BY plays")
for row in cur:
    print(row)

# cur.execute("DELETE FROM Tracks WHERE plays < 100")
# cur.execute("DELETE FROM Tracks WHERE title != 'Thunderstruck'")
# cur.execute("DELETE FROM Tracks WHERE title != 'My Way'")
# cur.execute("DELETE FROM Tracks WHERE title = 'My Way'")
# cur.execute("DELETE FROM Tracks WHERE title = 'Thunderstruck'")

# cur.execute("UPDATE Tracks SET plays = 16 WHERE title = 'My Way'")
# cur.execute("UPDATE Tracks SET plays = 30 WHERE title = 'Thunderstruck'")
# cur.execute("UPDATE Tracks SET title = 'My Love' WHERE title = 'My Way'")
# cur.execute("UPDATE Tracks SET title = 'Love-Thunder' WHERE title = 'Thunderstruck'")
# cur.execute("UPDATE Tracks SET plays = 30")
conn.commit()

cur.close()
# conn.close() """

# HERE IS THE SOURCE CODE FOR OUR TWITTER SPIDERING APPLICATION:
from urllib.request import urlopen
import urllib.error
import urllib.parse
from twitter import twurl
import oauth
import hidden
import json
import ssl

# TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# conn = sqlite3.connect("spider.sqlite")
# cur = conn.cursor()

# cur.execute("""
#             CREATE TABLE IF NOT EXISTS Twitter
#             (name TEXT, retrieved INTEGER, friends INTEGER)""")

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# while True:
#     acct = input("Enter a Twitter account, or quit: ")
#     if (acct == 'quit'): break
#     if (len(acct) < 1): 
#         cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
#         try:
#             acct = cur.fetchone()[0]
#         except:
#             print('No unretrieved Twitter accounts found')
#             continue
        
#     url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'})
#     print('Retrieving', url)
#     connection = urlopen(url, context=ctx)
#     data = connection.read().decode()
#     headers = dict(connection.getheaders())
    
#     print('Remaining', headers['x-rate-limit-remaining'])
#     js = json.loads(data)
#     # Debugging
#     # print(json.dumps(js, index=4))
    
#     cur.execute("UPDATE Twitter SET retrieved=1 WHERE name = ?", (acct, ))
    
#     countnew = 0
#     countold = 0
#     for u in js['users']:
#         friend = u['screen_name']
#         print(friend)
#         cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend))
        
#         try:
#             count = cur.fetchone()[0]
#             cur.execute("UPDATE Twitter SET friends = ? WHERE name = ?", 
#                         (count+1, friend))
#             countold = countold + 1
#         except:
#             cur.execute('''
#                         INSERT INTO Twitter (name, retrieved, friends)
#                         VALUES(?, 0, 1)''', (friend, ))
#             countnew = countnew + 1
#     print("New accounts=", countnew, " revisited=", countold)
#     conn.commit()

# cur.close()

# At this point, we might want to write a simple database dumper to take a look at 
# what is in our spider.sqlite file:
""" conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()
cur.execute('SELECT * FROM Twitter')
count = 0
for row in cur:
    print(row)
    count = count + 1
print(count, 'rows.')
cur.close() """

# 15.8 PROGRAMMING WITH MULTIPLE TABLES
# We will now redo the Twitter spider program using two tables, the primary keys, 
# and the key references as described above. Here is the code for the new version of 
# the program:
# TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# conn = sqlite3.connect('friends.sqlite')
# cur = conn.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS People
#             (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
# cur.execute('''CREATE TABLE IF NOT EXISTS Follows
#             (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# while True:
#     acct = input('Enter a Twitter account, or quit: ')
#     if (acct == 'quit'): break
#     if (len(acct) < 1):
#         cur.execute(
#             'SELECT id, name FROM People WHERE retrieved=0 LIMIT 1'
#         )        
#         try:
#             (id, acct) = cur.fetchone()
#         except:
#             print('No unretrieved Twitter accounts found')
#             continue
#     else:
#         cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1', (acct, ))
#         try:
#             id = cur.fetchone()[0]
#         except:
#             cur.execute('''INSERT OR IGNORE INTO People
#                         (name, retrieved) VALUES(?, 0) ''', (acct, ))
#             conn.commit()
#             if cur.rowcount != 1:
#                 print('Error inserting account:', acct)
#                 continue
#             id = cur.lastrowid
    
#     url = twurl.augment(TWITTER_URL,
#                         {'screen_name': acct, 'count': 100})
#     print('Retrieving account', acct)
#     try:
#         connection = urllib.request.urlopen(url, context=ctx)
#     except Exception as err:
#         print('Failed to Retrieve', err)
#         break
    
#     data = connection.read().decode()
#     headers = dict(connection.getheaders())

#     print('Remaining', headers['x-rate-limit-remaining'])

#     try:
#         js = json.loads(data)
#     except:
#         print('Unable to parse json')
#         print(data)
#         break

#     # Debugging
#     # print(json.dumps(js, indent=4))

#     if 'users' not in js:
#         print('Incorrect JSON received')
#         print(json.dumps(js, indent=4))
#         continue
    
#     cur.execute('UPDATE People SET retrieved=1 WHERE name = ?', (acct, ))

#     countnew = 0
#     countold = 0
#     for u in js['users']:
#         friend = u['screen_name']        
#         print(friend)
#         cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1', (friend, ))

#         try:
#             friend_id = cur.fetchone()[0]
#             countold = countold + 1
#         except:
#             cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
#                         VALUES (?, 0)''', (friend, ))
#             conn.commit()
#             if cur.rowcount != 1:
#                 print('Error inserting account:', friend)
#                 continue
#             friend_id = cur.lastrowid
#             countnew = countnew + 1    
#         cur.execute('''INSERT OR IGNORE INTO Follows (from_id, to_id)
#                     VALUES(?, ?)''', (id, friend_id))
#     print('New accounts=', countnew, ' revisited=', countold)
#     print('Remaining', headers['x-rate-limit-remaining'])
#     conn.commit()
# cur.close()
            
# The following code demonstrates the data that we will have in the database after 
# the multi-table Twitter spider program (above) has been run several times.          
conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM People')
count = 0
print('People:')
for row in cur:
    if (count < 5): print(row)
    count = count + 1
print(count, 'rows.')

cur.execute('SELECT * FROM Follows')
count = 0
print("Follows:")
for row in cur:
    if (count < 5): print(row)
    count = count + 1
print(count, 'rows.')

cur.execute('''SELECT * FROM Follows JOIN People
            ON Follows.to_id = People.id
            WHERE Follows.from_id = 2''')
count = 0
print('Connections for id=2')
for row in cur:
    if (count < 5): print(row)
    count = count + 1
print(count, 'rows.')

cur.close()
    








                
                
                
                