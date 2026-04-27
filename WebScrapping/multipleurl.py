import requests
from bs4 import BeautifulSoup

urls = [
    "https://www.python.org/",
    "https://numpy.org/",
    "https://pandas.pydata.org/"
]

for url in urls:
    response = requests.get(url)
    content = response.text
    heading = BeautifulSoup(content, "html.parser")
    print(heading.title.text)