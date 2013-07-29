# This Python file uses the following encoding: utf-8

import xlrd

filePath = '/home/cutejumper/Downloads/movie_view.xls'
# filePath = '/home/cutejumper/Downloads/boxoffice.xls'
boxFilePath = '/home/cutejumper/Downloads/boxoffice.xls'

data = xlrd.open_workbook(str(filePath))
table = data.sheet_by_index(2)
# table = data.sheet_by_index(0)
nrows = table.nrows
print nrows

boxData = xlrd.open_workbook(str(boxFilePath))
boxTable = boxData.sheet_by_index(0)
boxnrows = boxTable.nrows
boxMovieName = []
filterName = []
for rownum in range(1, boxnrows):
    boxMovieName.append(boxTable.row_values(rownum)[0].encode('utf-8'))
    filterName = list(set(boxMovieName))
    filterName.sort(key=boxMovieName.index)

for name in filterName:
    print name + '\n'

print len(filterName)

movieMap = {}
for rownum in range(1, nrows):
    movieName = table.row_values(rownum)[1].encode('utf-8')
    # movieName = str(table.row_values(rownum)[0].encode('gbk'))
    print type(movieName)
    if movieName in filterName:
        movieDate = table.row_values(rownum)[9].encode('utf-8')
        movieMap[movieName] = movieDate

print type(movieMap)
print movieMap

movieDateMap = {}
# movieDict = [lambda value: value.replace('-', '') for value in movieMap.values()]
for key, value in movieMap.items():

    requestCounter = 0

    requestCounter += 1

    print key + '--->' + value + '\n'
    valueList = str(value).split('-')
    valueIntList = map(lambda value: int(value), valueList)
    # print valueList
    print valueIntList
    dataSum = valueIntList[0]*12 + valueIntList[1]
    newSum = dataSum-4
    # valueIntList[0] = newSum / 12
    # valueIntList[1] = newSum % 12
    year = newSum / 12
    month = newSum % 12
    oldDate = str(year) + '-' + str(month) + '-' + str(valueIntList[2]) + '-0'
    newSum = dataSum+4
    year = newSum /12
    month = newSum % 12
    newDate = str(year) + '-' + str(month) + '-' + str(valueIntList[2]) + '-0'

    finalDate = oldDate + ':' + newDate

    requestCounter = 0

    print finalDate
    movieDateMap[key] = finalDate
    # print oldDate
    # print newDate

# print movieDateMap
for key, value in movieDateMap.items():
    print str(key) + '--->' + str(value)
print len(movieDateMap)
# print len(movieMap)
# print movieDict