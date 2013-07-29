# This Python file uses the following encoding: utf-8
# __author__ = 'cutejumper'

import re
import urllib2
from BeautifulSoup import BeautifulSoup

proxy_support = urllib2.ProxyHandler({'http': 'http://127.0.0.1:8087'})
opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
content = urllib2.urlopen('http://www.baidu.com').read()
print content