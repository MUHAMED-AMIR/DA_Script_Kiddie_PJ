
#using request libary
import requests

#Set Target Webpage
url = 'http://192.168.80.130/multi'
r = requests.get(url)
#print(r.text)
#this will get the status code
print('Status Code: ')
print("\t*",r.status_code)
#this will just get the headers
h = requests.head(url)
print("Header:")
print("************")
#To print this line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

headers= {
    'User-Agent':"Mobile"
}
#Test of a modified user-agent
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2,headers=headers)
print(rh.text)


