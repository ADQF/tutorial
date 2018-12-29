import re
import urllib.request
url = 'http://example.python-scraping.com/places/default/view/United-States-234'
html = urllib.request.urlopen(url).read()
re.findall('<td class="w2p_fw">(.*?)</td>', html)


