#!/usr/bin/python3
import cgi,cgitb
cgitb.enable()

#to receive data from web httpd protocol
print("Content-type:text/html")
print("")

html_data=cgi.FieldStorage()
# only looking for form data and those variables data as well

select=html_data.getvalue('s')
#print(username)
#print(password)
if select == "whp" :
    print("<meta http-equiv='refresh' content='1;url=http://35.154.135.65/whp.html'>")
    
else :
    print("<meta http-equiv='refresh' content='1;url=http://35.154.135.65/whm.html'>")

