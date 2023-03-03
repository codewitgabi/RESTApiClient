from django.shortcuts import render, redirect
import requests
import json


def index(request):
	if request.method == "POST":
		method = request.POST.get("method")
		endpoint = request.POST.get("endpoint")
		headers = json.loads(request.POST.get("headers")) if request.POST.get("headers") else {}
		data = json.loads(request.POST.get("data")) if request.POST.get("data") else {}
		
		try:
			if method == "GET":
				response = requests.get(endpoint, headers=headers)
				status_code = response.status_code
				response = response.json()
				
			elif method == "POST":
				response = requests.post(endpoint, headers=headers, data=data)
				status_code = response.status_code
				response = response.json()
			
			elif method == "PUT":
				response = requests.put(endpoint, headers=headers, data=data)
				status_code = response.status_code
				response = response.json()
			
			elif method == "PATCH":
				response = requests.patch(endpoint, headers=headers, data=data)
				status_code = response.status_code
				response = response.json()
				
			elif method == "OPTIONS":
				response = requests.options(endpoint, headers=headers)
				status_code = response.status_code
				response = response.json()
			
			elif method == "HEAD":
				response = requests.head(endpoint, headers=headers)
				status_code = response.status_code
				response = response.headers
				
		except Exception as e:
			response = e
		
		context = {
			"response": response,
			"status_code": status_code,
		}
		return render(request, "index.html", context)
		
	return render(request, "index.html")

