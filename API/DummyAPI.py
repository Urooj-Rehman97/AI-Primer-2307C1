import requests

url = 'https://dummyjson.com/quotes'
response = requests.get(url)

data = response.json()
# print(data)

for q in data["quotes"][:10]:
    print("-",q["quote"])
    print("-",q["author"])
