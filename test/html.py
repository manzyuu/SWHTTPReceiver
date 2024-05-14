from bs4 import BeautifulSoup
import requests

url = "http://manzyuu-server.duckdns.org:8000/"
response = requests.get(url)
contents = response.content
#HTMLを元に、オブジェクトを作る
soup = BeautifulSoup(contents, "html.parser")
print(soup)