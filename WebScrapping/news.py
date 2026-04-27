import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headline = soup.find_all("h2")
print("Latest News Headlines: \n")

for h in headline[:5]:
    print("-", h.text.strip())