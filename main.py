import requests
from bs4 import BeautifulSoup


base_url = 'http://minhateca.com.br'
url = '' #'http://minhateca.com.br/FOLDER'
filename =  'links'


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
            #print (f['href'], f.get_text())
        return urls_dict


a = tecaCrawler(url, base_url)
dictlist = [[key, value] for key, value in a.items()]
with open(filename, 'w+', 1) as logfile:
    logfile.write('name' + ' ; ' + 'link' + '\n')
    for i in dictlist:
        logfile.write(i[0]+' ; '+ i[1] + '\n')
