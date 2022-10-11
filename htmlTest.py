from bs4 import BeautifulSoup

# import requests
with open("test.html") as fhand:
    html_text = fhand.read()  # read file content
# print(html_text)

soup = BeautifulSoup(html_text, "html.parser")
for p in soup.find_all("p"):
    print(p.text)

print()
print(soup.find("p", {"id": "text"}).attrs["id"])

print(soup.find("body").main.p)

# print(soup.find_all("p")[1].text)
