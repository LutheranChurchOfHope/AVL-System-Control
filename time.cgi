#!/usr/bin/python3
# a cute, easy, simple code to display current server time to the end user's web page.
# use this code to diplay to a web page that a linux server is using the correct time
# location /var/www/cgi-bin

import cgitb
import datetime

cgitb.enable()

now = datetime.datetime.now()
print ("content-Type: text/html")
print ("")
print ("Server Date and Time:")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
