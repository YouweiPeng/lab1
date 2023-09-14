import requests

#print (requests.__version__)

response = response = requests.get('http://google.com/')
print(response.text)
