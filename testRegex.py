# This Python file uses the following encoding: utf-8
# __author__ = 'cutejumper'

import re

s = '123abc456eabc789'
print re.findall(r'abc', s)


# newRp = re.compile(r'[0-9,]')
html = 'sdhkas 10,344,192 sakdhak'
newhtml = html.replace(',', '')
print newhtml
newRp = re.compile(r'\b(?:\d)+')
print newRp.findall(newhtml)
print newRp.findall('10')