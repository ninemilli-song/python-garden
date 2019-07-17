#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
# res = requests.get('https://www.google.com/search?q='+' '.join(sys.argv[1:]))
res = requests.get('http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&ch=&tn=baiduerr&bar=&wd=python')
res.raise_for_status()

# Retrieve top search result links.
# print('res test: \n', res.text)
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
link_elems = soup.select('.result .c-title-en a')
print('link_elems: \n', link_elems)
numOpen = min(5, len(link_elems))
for i in range(numOpen):
    # webbrowser.open('http://google.com' + link_elems[i].get('href'))
    webbrowser.open(link_elems[i].get('href'))
