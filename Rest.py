import requests
#get request
# 

# response = requests.get(url)
# print(response.status_code)
# print(response.json())
# print(response.headers['Content-Type'])



#post request
# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "userId": 10,
#     "id": 10,
#     "title": "Title ..",
#     "body": "bar",
#     "completed": True
# }
# response = requests.post(url, json = data)
# print(response.status_code)
# print(response.json())

#put request
url = "https://jsonplaceholder.typicode.com/todos/1"
data = {
    "title": "Little Title.",
}
response = requests.put(url, json = data)
print(response.status_code)
print(response.json())
