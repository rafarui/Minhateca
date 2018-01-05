import argparse
from core.crawler import tecaCrawler

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--folderurl', action = 'store', dest = 'url',required = True, help = 'Minhateca folder URL')
parser.add_argument('-o', '--output', action = 'store', dest = 'filename', required = True, help = 'file name')
args = parser.parse_args()

base_url = 'http://minhateca.com.br'
url = args.url
filename = args.filename

a = tecaCrawler(url, base_url)
dictlist = [[key, value] for key, value in a.items()]
with open(filename, 'w+', 1) as logfile:
    logfile.write('name' + ' ; ' + 'link' + '\n')
    for i in dictlist:
        logfile.write(i[0]+' ; '+ i[1] + '\n')
