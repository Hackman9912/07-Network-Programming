import requests
r = requests.get('https://api.github.com/user', auth=('charleshackett89@gmail.com', 'PASSWORD'))
print(r.status_code)
print(r.url)
print(r.request)
