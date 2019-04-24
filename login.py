#!/usr/bin/env python3

import cgi
import cgitb
from http import cookies
import urllib.parse
import mysql.connector
from mysql.connector import errorcode


cgitb.enable() #provides additional security by not revealing innerworkings of code to the outside

form = cgi.FieldStorage() #instantiates the form data

username = form.getvalue('username')
password = form.getvalue('password')

conn = mysql.connector.connect(user='m201842', password = 'Bandit', host='midn.cyber.usna.edu', database='m201842')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Users WHERE Username=" + username + " AND PasswordHashes="+password)
if cursor.rowcount == 0:
    print("Content-Type: text/html")
    print()
    print('''\
    <html>
        <head>
            <script>
                alert("Invalid username and password");
            </script>
            <meta http-equiv="refresh" content="0;url=signup.html"/>
        </head>
    </html>
    ''')

else:
    #set cookies
    #set expiration time
    expires = 60*60;

    cookie = cookies.SimpleCookie()
    cookie["sessionID"] = urllib.parse.quote(Math.random())
    cookie["username"] = urllib.parse.quote(username)
    cookie["username"]['expires'] = expires

    #redirects to the message board
    print("Content-Type: text/html")
    print()
    print('''\
    <html>
        <head>
            <script>
                alert("You are now signed in as "+username);
            </script>
            <meta http-equiv="refresh" content="0;url=messageboard.py"/>
        </head>
    </html>
    ''')
