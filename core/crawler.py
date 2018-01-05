import requests
from bs4 import BeautifulSoup

def tecaCrawler(url, base_url):
    urls_dict = {}
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    files = soup.find("div", {"id": "foldersList"})
    if files is None:
        files = soup.find_all("a", {"class": "expanderHeader downloadAction"})
        for f in files:
            urls_dict.update({f.get_text().strip(): base_url + f["href"]})
        return urls_dict
    else:
        for f in files.find_all('a'):
            tt = tecaCrawler(base_url + f['href'],base_url )
            urls_dict.update(tt)
        return urls_dict