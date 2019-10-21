#!/usr/bin/python3
import cgi,cgitb
cgitb.enable()

#to receive data from web httpd protocol
print("Content-type:text/html")
print("")

html_data=cgi.FieldStorage()
# only looking for form data and those variables data as well

tech=html_data.getvalue('t')
#print(username)
#print(password)
if tech == "docker" :
    print("<meta http-equiv='refresh' content='1;url=http://35.154.135.65/docker.html'>")
    
else :
    print("<meta http-equiv='refresh' content='1;url=http://35.154.135.65/aws.html'>")


