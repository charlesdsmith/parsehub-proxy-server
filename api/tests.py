import os
import unittest
import requests
from routes import app
from initialize import db
import json
import uuid

basedir = os.path.abspath(os.path.dirname(__file__))


class TestCase(unittest.TestCase): 
    def test_get(self):

        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Host": "httpbin.org",
            "User-Agent": "curl/7.35.0",
        }

        response = requests.get("http://localhost:5000/proxy/http://youtube.com", headers=headers)
        expected = 200
        assert expected == response.status_code
  
    def test_post(self):
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Host": "httpbin.org",
            "User-Agent": "curl/7.35.0",
            "Content-Type":"application/x-www-form-urlencoded"
            }
        
        form = {
            "test": "data"
        }

        response = requests.post("http://localhost:5000/proxy/http://httpbin.org/post", headers=headers, data=form)
        expected = 200
        assert expected == response.status_code
    
    def test_get_404(self):

        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Host": "httpbin.org",
            "User-Agent": "curl/7.35.0",
        }

        response = requests.get("http://localhost:5000/proxy/http://httpbin.org/fake-url", headers=headers)
        expected = 404
        assert expected == response.status_code
    
    def test_post_404(self):
        headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Host": "httpbin.org",
                "User-Agent": "curl/7.35.0",
                "Content-Type":"application/x-www-form-urlencoded"
                }

        form = {
            "test": "data"
        }
        response = requests.post("http://localhost:5000/proxy/http://httpbin.org/fake-url", headers=headers, data=form)
        expected = 404
        assert expected == response.status_code
    

if __name__ == '__main__':
    unittest.main()
