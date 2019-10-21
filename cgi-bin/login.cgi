#!/usr/bin/python3
import cgi

#to receive data from web httpd protocol
print("Content-type:text/html")
print("")

html_data=cgi.FieldStorage()
# only looking for form data and those variables data as well

username=html_data.getvalue('u')
password=html_data.getvalue('p')
#print(username)
#print(password)
if username == 'adhoc' and password == 'devops' :
    print("<meta http-equiv='refresh' content='1;url=http://35.154.135.65/service.html'>")
    
else :
    print("<meta http-equiv='refresh' content='1;url=http://35.154.135.65/deny.html'>")

