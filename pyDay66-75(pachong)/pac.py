import bs4

exFile = open('ex.html')
exSoup = bs4.BeautifulSoup(exFile.read())
elems = exSoup.select('#author')
