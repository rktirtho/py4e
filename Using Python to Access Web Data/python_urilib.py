import urllib.request, urllib.parse ,  urllib.error

fHand =  urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fHand:
    print(line)