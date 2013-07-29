# This Python file uses the following encoding: utf-8
# __author__ = 'cutejumper'

import numpy
import pylab
from pylab import savefig
import xlwt
movieSearchFile = './movieSearchNum.txt'
movieBoxofficeFile = 'totalboxoffice.txt'
weekSearchFile = 'weekSearchNum.txt'
weekBoxofficeFile = 'weekboxoffice.txt'

movieSearchObj = open(movieSearchFile, 'r')
movieBoxofficeObj = open(movieBoxofficeFile, 'r')
weekSearchObj = open(weekSearchFile, 'r')
weekBoxofficeObj = open(weekBoxofficeFile, 'r')

# print movieSearchObj.read()
# print movieBoxofficeObj.read()
# print weekSearchObj.read()
# print weekBoxofficeObj.read()

movieSearchDictList = []
movieSearchList = movieSearchObj.readlines()
for item in movieSearchList:
    movieName = item.split('-')[0]
    movieSearch = item.split('-')[1]
    # print str(movieName) + '--->' + str(movieSearch)
    movieSearchDictList.append([str(movieName), str(movieSearch)])

for moviesearch in movieSearchDictList:
    print moviesearch[0] + '--->' + moviesearch[1]

searchList = [search[1] for search in movieSearchDictList]
nameList = [search[0] for search in movieSearchDictList]
finalList = map(lambda x: int(x), searchList)
xlim = len(finalList)
ylim = max(finalList)

boxofficeDictList = []
boxofficeList = movieBoxofficeObj.readlines()
for item in boxofficeList:
    movieName = item.split('-')[0]
    movieBoxoffice = item.split('-')[1]
    boxofficeDictList.append([str(movieName), str(movieBoxoffice)])

officeList = [office[1] for office in boxofficeDictList]
finalofficelist = map(lambda x: int(x), officeList)
y1lim = max(finalofficelist)
x1lim = len(finalofficelist)
adjustofficelist = map(lambda x: (x*ylim)/y1lim, finalofficelist)

# print 'xlim' + str(xlim)
# print 'x1lim' + str(x1lim)
print 'y1lim' + str(y1lim)
print 'ylim' + str(ylim)
finalylim = max([ylim, y1lim])

weekSearchList = weekSearchObj.readlines()
weekBoxofficeList = weekBoxofficeObj.readlines()

weekSearchQuantity = []
for item in weekSearchList:
    weekSearchQuantity.append(int(item.split('-')[-1]))
    print int(item.split('-')[-1])

weekBoxofficeQuantity = []
for item in weekBoxofficeList:
    weekBoxofficeQuantity.append(int(item.split('-')[-1]))

weekxlim = len(weekSearchQuantity)
weekylim = max(weekSearchQuantity)
weekx1lim = len(weekBoxofficeQuantity)
weeky1lim = max(weekBoxofficeQuantity)
# weekmaxlim = max([weekylim, weeky1lim])

print 'weekxlim' + str(weekxlim)
print 'weekx1lim' + str(weekx1lim)
print 'weekylim' + str(weekylim)
print 'weeky1lim' + str(weeky1lim)

adjustWeekOfficeQuantity = map(lambda x: (x*weekylim)/weeky1lim, weekBoxofficeQuantity)

# x = [1, 2, 3, 4, 5]# Make an array of x values
# y = [1, 4, 9, 16, 25]# Make an array of y values for each x value
# x = [item for item in range(0, xlim)]
# y = adjustofficelist
# pylab.plot(x, y, color='r', linestyle='-', marker='o')# use pylab to plot x and y
# pylab.title('Plot of y vs. x')# give plot a title
# pylab.xlabel('x axis')# make axis labels
# pylab.ylabel('y axis')
# pylab.xlim(0.0, xlim)# set axis limits
# pylab.ylim(0.0, ylim)
# pylab.annotate(u"STSong华文宋体", fontproperties='STSong', xy=(3, -3))
# pylab.show()# show the plot on the screen
fig1 = pylab.figure(1)
x1 = [item for item in range(0, xlim)]# Make x, y arrays for each graph
y1 = finalList
x2 = [item for item in range(0, xlim)]
y2 = adjustofficelist
pylab.plot(x1, y1, color='r', linestyle='-', marker='o')# use pylab to plot x and y
pylab.plot(x2, y2, color='g', linestyle='-', marker='o')
pylab.title('Plot of y vs. x')# give plot a title
pylab.xlabel('x axis')# make axis labels
pylab.ylabel('y axis')
pylab.xlim(0.0, xlim)# set axis limits
pylab.ylim(0.0, ylim)
# pylab.show()# show the plot on the screen
fig1.savefig('clea.png')

fig2 = pylab.figure(2)
x1 = [item for item in range(0, weekxlim)]
y1 = weekSearchQuantity
x2 = [item for item in range(0, weekxlim)]
y2 = adjustWeekOfficeQuantity
pylab.plot(x1, y1, color='r', linestyle='-', marker='o')# use pylab to plot x and y
pylab.plot(x2, y2, color='g', linestyle='-', marker='o')
pylab.title('Plot of y vs. x')# give plot a title
pylab.xlabel('x axis')# make axis labels
pylab.ylabel('y axis')
pylab.xlim(0.0, weekxlim)# set axis limits
pylab.ylim(0.0, weekylim)
# pylab.show()# show the plot on the screen
fig2.savefig('clea2.png')