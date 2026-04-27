import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
response = requests.get(url)
# print(response.text)
code = response.text
with open("python.html",'w', encoding="utf-8") as file:
    file.write(code)
content = response.text
soup = BeautifulSoup(content, "html.parser")

print(soup.title)
print(soup.title.text)
print(soup.find("h1"))
print(soup.find("p"))
print(soup.find_all("p"))