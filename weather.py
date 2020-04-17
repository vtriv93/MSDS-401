import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid=8d2351c39c1fbec244c8a59227424628&units=imperial', auth=('user', 'pass'))
print(r.status_code)
print(r.json())
j=r.json()
print(j['main'])