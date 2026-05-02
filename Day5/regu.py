import requests
url="https://jsonplaceholder.typicode.com/posts"
response=requests.get("https://jsonplaceholder.typicode.com/posts")
 
print(type(response))
print(response.status_code)