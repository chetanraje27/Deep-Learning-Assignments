import requests

url = "http://127.0.0.1:8000/predict"
data = {"text": "I love"}

response = requests.post(url, json=data)
print(response.json())

data2 = {"text": "machine learning"}
response2 = requests.post(url, json=data2)
print(response2.json())