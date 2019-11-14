import requests
import json
def test(url):

    headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "curl/7.35.0",
  }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    return response

def test2(url):

    headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "curl/7.35.0",
    "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "test": "hello",
        "test2": "hello2"
    }

    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    return response


test2("http://localhost:5000/proxy/http://httpbin.org/fakeffs")
#test("http://localhost:5000/proxy/http://httpbin.org/get")

