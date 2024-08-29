import requests

url = requests.post("https://jsonplaceholder.typicode.com/posts")

print(url.text)
