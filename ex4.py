import requests

headers = {
    "User-Agent": "LupaBrowser/1.1",
}

res = requests.get("http://45.143.94.76:2020/task4?browser='LupaBrowser/1.1'", headers=headers)
print(res.text)