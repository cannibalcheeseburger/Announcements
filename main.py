import urllib.request
from bs4 import BeautifulSoup

url = "https://nith.ac.in/"

uClient = urllib.request.urlopen(url)
page_html = uClient.read()
uClient.close()

page_soup = BeautifulSoup(page_html,"html.parser")
announce_container = page_soup.find_all("ul",class_ = "allnithlinks")[0]
announcements = announce_container.find_all("a")

print("\n\nAnnoucements:\n\n")

for announce in announcements:
    print(announce.text.strip())
    if announce['href'] != "#":
        print("Link:",announce['href'],"\n\n")