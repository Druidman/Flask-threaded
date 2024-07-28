import requests


def test():
    response = requests.get("http://127.0.0.1:5000/wait")
    print(response.text)

test()
    