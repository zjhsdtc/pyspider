# This Python file uses the following encoding: utf-8
# __author__ = 'cutejumper'

import re
import urllib2
from BeautifulSoup import BeautifulSoup

movieName = '辛巴达历险记2013'
url = 'http://s.weibo.com/weibo/' + str(movieName) + '&timescope=custom:2013-1-31-0:2013-09-31-0&Refer=g'

print url

proxy_support = urllib2.ProxyHandler({'http': 'http://127.0.0.1:8087'})
opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

request = urllib2.Request(url)
request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0)')

response = urllib2.urlopen(request)
the_page = response.read()

print the_page

cleaSoup = BeautifulSoup(the_page)

scripts = cleaSoup.findAll('script')

# print scripts

# 这个为什么不行啊= =
# rp = re.compile(r'span class=\"W_textc\"(.*?)span')
rp = re.compile(r'W_textc(.*?)span')
result = rp.findall(str(scripts))
print result

newResult = result[-1]
print newResult
rp = re.compile(r' (.*?) ')
clea = rp.findall(newResult)
print clea
newClea = map(lambda item: item.replace(',', ''), clea)
print int(newClea[0])

'''rp = re.compile(r' (.*?) ')
itemlist = rp.findall(str(result))
print itemlist
newItemList = map(lambda x: x.replace(',', ''), itemlist)
print newItemList
rp = re.compile(r'\b(?:\d)+')
for item in newItemList:
    match = rp.match(str(item))
    if match:
        print str(item) + '   cleantha'
        '''
# print rp.findall(str(newItemList))

'''/usr/bin/python /home/cutejumper/Documents/pyBigData/filepredict/manage.py runserver 8000
Validating models...

0 errors found
July 07, 2013 - 05:10:13
Django version 1.5.1, using settings 'filepredict.settings'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
looping
人再囧途之泰囧
looping
人再囧途之泰囧
\"&gt;\u627e\u5230 809 \u6761\u7ed3\u679c&lt;\/
['809']
<type 'int'>
final result809
looping
一代宗师
\"&gt;\u627e\u5230 809 \u6761\u7ed3\u679c&lt;\/
['809']
<type 'int'>
final result809
looping
一代宗师
\"&gt;\u627e\u5230 4,919,280 \u6761\u7ed3\u679c&lt;\/
['4,919,280']
<type 'int'>
final result4919280
looping
007：大破天幕杀机'''

'''
http://s.weibo.com/weibo/%E4%BA%BA%E5%86%8D%E5%9B%A7%E9%80%94%E4%B9%8B%E6%B3%B0%E5%9B%A7&timescope=custom:2012-8-12-0:2013-4-12-0&Refer=g
http://s.weibo.com/weibo/%E4%BA%BA%E5%86%8D%E5%9B%A7%E9%80%94%E4%B9%8B%E6%B3%B0%E5%9B%A7&timescope=custom:2012-11-30-0:2013-4-5-0&Refer=g
'''

'''
/usr/bin/python /home/cutejumper/Documents/pyBigData/filepredict/manage.py runserver 8000
Validating models...

0 errors found
July 07, 2013 - 05:55:44
Django version 1.5.1, using settings 'filepredict.settings'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
looping
人再囧途之泰囧
\"&gt;\u627e\u5230 809 \u6761\u7ed3\u679c&lt;\/
['809']
<type 'int'>
final result809
looping
一代宗师
\"&gt;\u627e\u5230 4,919,280 \u6761\u7ed3\u679c&lt;\/
['4,919,280']
<type 'int'>
final result4919280
looping
007：大破天幕杀机
\"&gt;\u627e\u5230 1,039,888 \u6761\u7ed3\u679c&lt;\/
['1,039,888']
<type 'int'>
final result1039888
looping
云图
\"&gt;\u627e\u5230 5,093,968 \u6761\u7ed3\u679c&lt;\/
['5,093,968']
<type 'int'>
final result5093968
looping
特警判官
\"&gt;\u627e\u5230 183 \u6761\u7ed3\u679c&lt;\/
['183']
<type 'int'>
final result183
looping
午夜微博
\"&gt;\u627e\u5230 593 \u6761\u7ed3\u679c&lt;\/
['593']
<type 'int'>
final result593
looping
101次求婚
\"&gt;\u627e\u5230 704 \u6761\u7ed3\u679c&lt;\/
['704']
<type 'int'>
final result704
looping
霍比特人1：意外之旅
\"&gt;\u627e\u5230 207,648 \u6761\u7ed3\u679c&lt;\/
['207,648']
<type 'int'>
final result207648
looping
劫案迷云
\"&gt;\u627e\u5230 387,280 \u6761\u7ed3\u679c&lt;\/
['387,280']
<type 'int'>
final result387280
looping
逆世界
\"&gt;\u627e\u5230 1,819,660 \u6761\u7ed3\u679c&lt;\/
['1,819,660']
<type 'int'>
final result1819660
looping
笑功震武林
\"&gt;\u627e\u5230 363,163 \u6761\u7ed3\u679c&lt;\/
['363,163']
<type 'int'>
final result363163
looping
楼
\"&gt;\u627e\u5230 82,658,394 \u6761\u7ed3\u679c&lt;\/
['82,658,394']
<type 'int'>
final result82658394
looping
生化危机5：惩罚
\"&gt;\u627e\u5230 73 \u6761\u7ed3\u679c&lt;\/
['73']
<type 'int'>
final result73
looping
铁娘子：坚固柔情
\"&gt;\u627e\u5230 85,696 \u6761\u7ed3\u679c&lt;\/
['85,696']
<type 'int'>
final result85696
looping
爱情银行
\"&gt;\u627e\u5230 359,800 \u6761\u7ed3\u679c&lt;\/
['359,800']
<type 'int'>
final result359800
looping
北京遇上西雅图
\"&gt;\u627e\u5230 8,536,587 \u6761\u7ed3\u679c&lt;\/
['8,536,587']
<type 'int'>
final result8536587
looping
魔境仙踪
\"&gt;\u627e\u5230 778,928 \u6761\u7ed3\u679c&lt;\/
['778,928']
<type 'int'>
final result778928
looping
毒战
\"&gt;\u627e\u5230 3,067,089 \u6761\u7ed3\u679c&lt;\/
['3,067,089']
<type 'int'>
final result3067089
looping
厨子戏子痞子
\"&gt;\u627e\u5230 1,544,940 \u6761\u7ed3\u679c&lt;\/
['1,544,940']
<type 'int'>
final result1544940
looping
忠烈杨家将
\"&gt;\u627e\u5230 3,847,303 \u6761\u7ed3\u679c&lt;\/
['3,847,303']
<type 'int'>
final result3847303
looping
虎胆龙威5
\"&gt;\u627e\u5230 873 \u6761\u7ed3\u679c&lt;\/
['873']
<type 'int'>
final result873
looping
叶问：终极一战
\"&gt;\u627e\u5230 116 \u6761\u7ed3\u679c&lt;\/
['116']
<type 'int'>
final result116
looping
巨人捕手杰克
\"&gt;\u627e\u5230 196,715 \u6761\u7ed3\u679c&lt;\/
['196,715']
<type 'int'>
final result196715
looping
止杀令
\"&gt;\u627e\u5230 89 \u6761\u7ed3\u679c&lt;\/
['89']
<type 'int'>
final result89
looping
爱神
\"&gt;\u627e\u5230 3,612,323 \u6761\u7ed3\u679c&lt;\/
['3,612,323']
<type 'int'>
final result3612323
looping
分手合约
\"&gt;\u627e\u5230 2,356,212 \u6761\u7ed3\u679c&lt;\/
['2,356,212']
<type 'int'>
final result2356212
looping
人间蒸发
\"&gt;\u627e\u5230 1,912,310 \u6761\u7ed3\u679c&lt;\/
['1,912,310']
<type 'int'>
final result1912310
looping
变身超人
\"&gt;\u627e\u5230 1,599,163 \u6761\u7ed3\u679c&lt;\/
['1,599,163']
<type 'int'>
final result1599163
looping
中国合伙人
\"&gt;\u627e\u5230 7,120,863 \u6761\u7ed3\u679c&lt;\/
['7,120,863']
<type 'int'>
final result7120863
looping
同谋
\"&gt;\u627e\u5230 1,815,654 \u6761\u7ed3\u679c&lt;\/
['1,815,654']
<type 'int'>
final result1815654
looping
钢铁侠3
\"&gt;\u627e\u5230 9,403,783 \u6761\u7ed3\u679c&lt;\/
['9,403,783']
<type 'int'>
final result9403783
looping
被解救的姜戈
\"&gt;\u627e\u5230 792,246 \u6761\u7ed3\u679c&lt;\/
['792,246']
<type 'int'>
final result792246
looping
遗落战境
\"&gt;\u627e\u5230 317,153 \u6761\u7ed3\u679c&lt;\/
['317,153']
<type 'int'>
final result317153
looping
亲爱
\"&gt;\u627e\u5230 74,502,261 \u6761\u7ed3\u679c&lt;\/
['74,502,261']
<type 'int'>
final result74502261
looping
天机·富春山居图
\"&gt;\u627e\u5230 4,244,806 \u6761\u7ed3\u679c&lt;\/
['4,244,806']
<type 'int'>
final result4244806
looping
杀戒
\"&gt;\u627e\u5230 178,011 \u6761\u7ed3\u679c&lt;\/
['178,011']
<type 'int'>
final result178011
looping
不二神探
\"&gt;\u627e\u5230 4,510,166 \u6761\u7ed3\u679c&lt;\/
['4,510,166']
<type 'int'>
final result4510166
looping
致命黑兰
\"&gt;\u627e\u5230 311,673 \u6761\u7ed3\u679c&lt;\/
['311,673']
<type 'int'>
final result311673
looping
圣诞玫瑰
\"&gt;\u627e\u5230 359,358 \u6761\u7ed3\u679c&lt;\/
['359,358']
<type 'int'>
final result359358
looping
星际迷航：暗黑无界
\"&gt;\u627e\u5230 558,806 \u6761\u7ed3\u679c&lt;\/
['558,806']
<type 'int'>
final result558806
looping
枕边有张脸
\"&gt;\u627e\u5230 272,724 \u6761\u7ed3\u679c&lt;\/
['272,724']
<type 'int'>
final result272724
looping
辛巴达历险记2013
\"&gt;\u627e\u5230 904 \u6761\u7ed3\u679c&lt;\/
['904']
<type 'int'>
final result904
looping
逆光飞翔
\"&gt;\u627e\u5230 384,507 \u6761\u7ed3\u679c&lt;\/
['384,507']
<type 'int'>
final result384507
{'\xe9\xad\x94\xe5\xa2\x83\xe4\xbb\x99\xe8\xb8\xaa': 778928, '\xe5\xa4\xa9\xe6\x9c\xba\xc2\xb7\xe5\xaf\x8c\xe6\x98\xa5\xe5\xb1\xb1\xe5\xb1\x85\xe5\x9b\xbe': 4244806, '\xe6\x98\x9f\xe9\x99\x85\xe8\xbf\xb7\xe8\x88\xaa\xef\xbc\x9a\xe6\x9a\x97\xe9\xbb\x91\xe6\x97\xa0\xe7\x95\x8c': 558806, '\xe6\xad\xa2\xe6\x9d\x80\xe4\xbb\xa4': 89, '\xe9\x80\x86\xe5\x85\x89\xe9\xa3\x9e\xe7\xbf\x94': 384507, '\xe5\x90\x8c\xe8\xb0\x8b': 1815654, '\xe5\x88\x86\xe6\x89\x8b\xe5\x90\x88\xe7\xba\xa6': 2356212, '\xe5\xbf\xa0\xe7\x83\x88\xe6\x9d\xa8\xe5\xae\xb6\xe5\xb0\x86': 3847303, '\xe4\xb8\x8d\xe4\xba\x8c\xe7\xa5\x9e\xe6\x8e\xa2': 4510166, '\xe7\x94\x9f\xe5\x8c\x96\xe5\x8d\xb1\xe6\x9c\xba5\xef\xbc\x9a\xe6\x83\xa9\xe7\xbd\x9a': 73, '\xe4\xb8\xad\xe5\x9b\xbd\xe5\x90\x88\xe4\xbc\x99\xe4\xba\xba': 7120863, '\xe4\xba\xba\xe5\x86\x8d\xe5\x9b\xa7\xe9\x80\x94\xe4\xb9\x8b\xe6\xb3\xb0\xe5\x9b\xa7': 809, '\xe7\x89\xb9\xe8\xad\xa6\xe5\x88\xa4\xe5\xae\x98': 183, '\xe8\x87\xb4\xe5\x91\xbd\xe9\xbb\x91\xe5\x85\xb0': 311673, '\xe4\xba\xb2\xe7\x88\xb1': 74502261, '007\xef\xbc\x9a\xe5\xa4\xa7\xe7\xa0\xb4\xe5\xa4\xa9\xe5\xb9\x95\xe6\x9d\x80\xe6\x9c\xba': 1039888, '101\xe6\xac\xa1\xe6\xb1\x82\xe5\xa9\x9a': 704, '\xe5\x8d\x88\xe5\xa4\x9c\xe5\xbe\xae\xe5\x8d\x9a': 593, '\xe7\x88\xb1\xe7\xa5\x9e': 3612323, '\xe4\xb8\x80\xe4\xbb\xa3\xe5\xae\x97\xe5\xb8\x88': 4919280, '\xe5\x8a\xab\xe6\xa1\x88\xe8\xbf\xb7\xe4\xba\x91': 387280, '\xe9\x81\x97\xe8\x90\xbd\xe6\x88\x98\xe5\xa2\x83': 317153, '\xe6\xa5\xbc': 82658394, '\xe6\x9e\x95\xe8\xbe\xb9\xe6\x9c\x89\xe5\xbc\xa0\xe8\x84\xb8': 272724, '\xe9\x92\xa2\xe9\x93\x81\xe4\xbe\xa03': 9403783, '\xe5\xb7\xa8\xe4\xba\xba\xe6\x8d\x95\xe6\x89\x8b\xe6\x9d\xb0\xe5\x85\x8b': 196715, '\xe6\x9d\x80\xe6\x88\x92': 178011, '\xe6\xaf\x92\xe6\x88\x98': 3067089, '\xe7\x88\xb1\xe6\x83\x85\xe9\x93\xb6\xe8\xa1\x8c': 359800, '\xe8\x99\x8e\xe8\x83\x86\xe9\xbe\x99\xe5\xa8\x815': 873, '\xe8\xa2\xab\xe8\xa7\xa3\xe6\x95\x91\xe7\x9a\x84\xe5\xa7\x9c\xe6\x88\x88': 792246, '\xe4\xba\x91\xe5\x9b\xbe': 5093968, '\xe5\x8f\x98\xe8\xba\xab\xe8\xb6\x85\xe4\xba\xba': 1599163, '\xe9\x93\x81\xe5\xa8\x98\xe5\xad\x90\xef\xbc\x9a\xe5\x9d\x9a\xe5\x9b\xba\xe6\x9f\x94\xe6\x83\x85': 85696, '\xe5\x8c\x97\xe4\xba\xac\xe9\x81\x87\xe4\xb8\x8a\xe8\xa5\xbf\xe9\x9b\x85\xe5\x9b\xbe': 8536587, '\xe5\x8e\xa8\xe5\xad\x90\xe6\x88\x8f\xe5\xad\x90\xe7\x97\x9e\xe5\xad\x90': 1544940, '\xe7\xac\x91\xe5\x8a\x9f\xe9\x9c\x87\xe6\xad\xa6\xe6\x9e\x97': 363163, '\xe9\x9c\x8d\xe6\xaf\x94\xe7\x89\xb9\xe4\xba\xba1\xef\xbc\x9a\xe6\x84\x8f\xe5\xa4\x96\xe4\xb9\x8b\xe6\x97\x85': 207648, '\xe5\x9c\xa3\xe8\xaf\x9e\xe7\x8e\xab\xe7\x91\xb0': 359358, '\xe4\xba\xba\xe9\x97\xb4\xe8\x92\xb8\xe5\x8f\x91': 1912310, '\xe9\x80\x86\xe4\xb8\x96\xe7\x95\x8c': 1819660, '\xe5\x8f\xb6\xe9\x97\xae\xef\xbc\x9a\xe7\xbb\x88\xe6\x9e\x81\xe4\xb8\x80\xe6\x88\x98': 116, '\xe8\xbe\x9b\xe5\xb7\xb4\xe8\xbe\xbe\xe5\x8e\x86\xe9\x99\xa9\xe8\xae\xb02013': 904}
[07/Jul/2013 06:09:06] "GET /moviespider/ HTTP/1.1" 200 4
Validating models...

0 errors found
July 07, 2013 - 06:11:28
Django version 1.5.1, using settings 'filepredict.settings'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

'''