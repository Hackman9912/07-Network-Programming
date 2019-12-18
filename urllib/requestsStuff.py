import requests
'''
link = link = 'http://www.python-requests.org'
r = requests.get(link)

print(dir(r))
print(type(r))
print(r.url)
print(r.status_code)
print(r.history)
print(r.headers) # response headers ith info about server date etc
print(r.headers['Content-Type']) # Specific header information grab
print(r.request.headers) # request headers
print(r.encoding) # response encoding
print(r.content[0:400]) # 400 bytes of characters
print(r.text[0:400]) # same as above but text of the 400 substr

r = requests.get(link, stream=True) # raw response
print(type(r.raw)) # type of raw response that we obtained
print(r.raw.read(100)) # read the first 100 characters from the raw response

TO RUN ABOVE COMMENT BELOW
'''

link = 'https://feeds.citibikenyc.com/stations/stations.json'
response = requests.get(link).json()
for i in range(10): # read the 10 stationName from JSON response
    print('Station: ', response['stationBeanList'][i]['stationName'])

