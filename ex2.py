import requests

res = requests.post('http://45.143.94.76:2020/task2', data={'name': 'name'})
print(res.text)