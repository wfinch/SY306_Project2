#!/usr/bin/python3
# Names:        MIDN Kevin Nguyen
#               MIDN Walt Finch
#               MIDN Maggie Madigan
#               MIDN Frederick Bleakley
# Course:       SY306
# Description:  Project 01 - messageboard.py
#               Displays the content of the Messages table
#               Also allows for a user to submit a new message, which is then handled by CGI
#               and parsed into an INSERT query.
#
# References:   W3 Schools: https://www.w3schools.com/python/python_mysql_insert.asp
#

import cgi, cgitb
cgitb.enable()

import mysql.connector

import os, sys, urllib.parse
from http import cookies

# Set up webpage
print("Content-Type: text/html\n")
print("<!DOCTYPE html>")
print("<html><head>")
print("<title> MidYak Message Board </title>")
print('<link rel="stylesheet" type="text/css" href="styles.css"')
print("</head>")
print("<body>")

# Read cookie to see if user is logged in
if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    mycookie = cookies.SimpleCookie()
    mycookie.load(cookie_string)

    try:
        sessionIDCookie = urllib.parse.unquote(mycookie['sessionID'].value)
        usernameCookie = urllib.parse.unquote(mycookie['username'].value)
    except KeyError:
        name = ""


else: # user is not logged in
    print("<p> Error: Must be logged in! </p>")
    print("<p> <a href = 'default.html'> Return to Homepage </a>")
    sys.exit()

# Set up query for SQL database
mydb = mysql.connector.connect(
  host="midn.cyber.usna.edu",
  user="m201842",
  passwd="Bandit"
)

# We will be querying the table for all messages and sorting by time order
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Messages ORDER BY TimeMessage ASC")
myresult = mycursor.fetchall()

# Print all the messages in the Messages table
print("<table>")
for x in myresult:
  print("<tr> <td>" + x + "</td>")
print("</table>")

# Form to submit a new message
print('''
<form method="post" action="messageboard.py">
Enter your message:<textarea name=messageBox rows="1" cols="45"> What's on your mind? </textarea> <br>
<input type="submit" value="Submit Message">
<input type="reset" value="Clear Message">
</form>
''')

# Get the form response via CGI to post a new message
form = cgi.FieldStorage()
messageBox = form.getvalue("messageBox")

# Inserts the username and their message into the Messages database
sql = "INSERT INTO Messages (User, Message) VALUES (%s, %s)"
val = (usernameCookie, messageBox)
mycursor.execute(sql, val)
mydb.commit()

print("</body></html>")
