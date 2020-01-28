import requests

for i in range(1, 101):
    res = requests.post('http://45.143.94.76:2020/task6', data={'number': i})
    if not res.url.endswith('flag=No'):
        print(res.text)
        break