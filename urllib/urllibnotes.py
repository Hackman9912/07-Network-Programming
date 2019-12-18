'''import urllib.request
# print(dir(urllib.request)) # list features available for urllib.request

link = 'https://www.google.com'
linkRequest = urllib.request.urlopen(link) # open the link
print(type(linkRequest)) # object type

linkResponse = urllib.request.urlopen(link).read() # open the link and read the content
print(type(linkResponse))

print(linkRequest.getcode()) # can also use it as linkRequest.code or .status
print(linkRequest.code)

print(linkRequest.url) # can also use .geturl()
print(linkRequest._method)
print(linkRequest.getheaders())
print(linkRequest.getheader('Content-Type')) # get the content type
print(linkRequest.info()['Content-Type']) # same as above'''

#############################################


import urllib.request as request
import urllib.error as error
'''
try:
    request.urlopen('https://www.python.ogr')
except error.URLError as e:
    print('Error occured: ', e.reason)
'''
import urllib.parse as urlparse
# print(dir(urlparse)) # list features from urllib.parse

amazonURL = 'https://amazon.com/s/ref=nb_sb_moss?url=search-alias%3Dstripbooks-intl-ship&field-keywords=Pearson+Books'
# print(urlparse.urlsplit(amazonURL)) #split the amazon url
# print(urlparse.urlsplit(amazonURL).scheme)
# print(urlparse.urlparse(amazonURL))
data = {'param1':'value1', 'param2':'value2'}
# print(urlparse.urlencode(data))
# print(urlparse.parse_qs(urlparse.urlencode(data)))
# print(urlparse.urlencode(data).encode('utf-8'))
# print(urlparse.urljoin('http://localhost:8080/~cache/','datafile')) # create url

import urllib.robotparser as robot
par = robot.RobotFileParser()
par.set_url('https://www.samsclub.com/robots.txt')
par.read() # reading the URL content
print(par)

print(par.can_fetch('*', 'https://www.samsclub.com/friend'))



