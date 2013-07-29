# This Python file uses the following encoding: utf-8
# __author__ = 'cutejumper'

import xlrd
boxFilePath = '/home/cutejumper/Downloads/boxoffice.xls'
boxData = xlrd.open_workbook(str(boxFilePath))
boxTable = boxData.sheet_by_index(0)
boxnrows = boxTable.nrows

def adjustDate(datetime):
    if int(datetime[0]) == 0:
        date = int(datetime)
        month = date / 100
        day = date % 100
        dateStr = '2013-' + str(month) + '-' + str(day) + '-0'
        return dateStr
    else:
        date = int(datetime)
        month = date / 100
        day = date % 100
        dateStr = '2012-' + str(month) + '-' + str(day) + '-0'
        return dateStr

movieDateDict = {}
for rownum in range(1, boxnrows):
    movieName = boxTable.row_values(rownum)[0].encode('utf-8')
    movieStartDateSum = (boxTable.row_values(rownum)[6].encode('utf-8'))
    movieEndDateSum = (boxTable.row_values(rownum)[7].encode('utf-8'))
    movieStartDate = adjustDate(movieStartDateSum)
    movieEndDate = adjustDate(movieEndDateSum)

    # print movieStartDate
    # print movieEndDate
    if movieName in movieDateDict.keys():
        # print 'oh!!!!!' + str(movieName)
        # print movieDateDict[movieName]
        movieDateDict[movieName].append([movieStartDate, movieEndDate])
    else:
        movieDateDict[movieName] = [[movieStartDate, movieEndDate]]

for key, value in movieDateDict.items():
    for date in value:
        url = 'http://s.weibo.com/weibo/' + str(key) + '&timescope=custom:' + str(date[0]) + ':'+ str(date[1]) + '&Refer=g'
        print url


