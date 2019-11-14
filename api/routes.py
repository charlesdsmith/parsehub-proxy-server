# flask API
from flask import Flask, make_response, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy/<path:url>', methods=['GET', 'POST'])
def handle(url):
	try:
		if request.method == "POST":

			headers = {
			"User-Agent": request.headers["user-agent"]
				}
			
			data = request.form

			try:
				response = requests.post(url, headers=headers, data=data)
				return (response.content, response.status_code) # make sure to return relevant info from end-server
				
			except Exception as e:
				return make_response(e)
		
		if request.method == "GET":
			headers = {
			"User-Agent": request.headers["user-agent"]
				}

			try:
				response = requests.get(url, headers=headers)
				return (response.content, response.status_code)
			except Exception as e:
				return make_response(e)


	except Exception as e:
		return Response(status=500)