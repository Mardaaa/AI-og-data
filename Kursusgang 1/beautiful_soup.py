from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# print(soup.get_text())

# print(soup.find_all("img"))

image1, image2 = soup.find_all("img")
# print(image1["src"])
# print(image2["src"])
# print(soup.title.string)

######################### Exercises ################3
url = "http://olympus.realpython.org/profiles"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup)
base_url = "http://olympus.realpython.org"

for element in soup.find_all("a"):
    print(base_url + element["href"])


