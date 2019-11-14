import os
import unittest
import requests
from routes import app
from models import db
import json
import uuid

basedir = os.path.abspath(os.path.dirname(__file__))


class TestCase(unittest.TestCase):
    def setUp(self):

        with app.app_context():
            app.config['TESTING'] = True
            app.config['WTF_CSRF_ENABLED'] = False
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
            app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            self.app = app.test_client()
            db.init_app(app)
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
            
    
    def test_get(self):

        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Host": "httpbin.org",
            "User-Agent": "curl/7.35.0",
        }

        response = requests.get("http://localhost:5000/proxy/http://youtube.com", headers=headers)
        print("RESPONSE TEXT", response.status_code)
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
            "test":"data"
        }

        response = requests.post("http://localhost:5000/proxy/http://httpbin.org/post", headers=headers, data=form)
        print("RESPONSE TEXT", response.status_code)
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
        print("RESPONSE TEXT", response.status_code)
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
        print("RESPONSE TEXT", response.status_code)
        expected = 404
        assert expected == response.status_code
    

if __name__ == '__main__':
    unittest.main()
