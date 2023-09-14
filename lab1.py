import requests

#print (requests.__version__)

response = response = requests.get('https://raw.githubusercontent.com/YouweiPeng/lab1/main/lab1.py')
print(response.text)
