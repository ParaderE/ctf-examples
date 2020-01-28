import requests

res = requests.request('LUPA', 'http://45.143.94.76:2020/task3')
print(res.text)