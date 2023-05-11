# imports
import http.client


conn = http.client.HTTPSConnection("www.uci.edu")
conn.request("GET","/")
resp=conn.getresponse()
content=resp.read(1000)      
print(content)


# close connection
conn.close()

