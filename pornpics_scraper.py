from bs4 import BeautifulSoup
import requests
import sys
import urllib.request

url = sys.argv[1]

# parse the page
page_raw = requests.get(url)
html = BeautifulSoup(page_raw.text, 'html.parser')

# find list of images in the DOM
image_list = html.find("ul", {"id": "tiles"})
list_items = image_list.find_all("li")

i = 1
for item in list_items:
    link = item.find("a")
    href = link["href"]
    
    urllib.request.urlretrieve(href, str(i).zfill(4) + ".jpg")

    i = i + 1

print("Finished scraping: " + str(i - 1) + " images")
