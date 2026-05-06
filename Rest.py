import requests
#get request
# url = "https://jsonplaceholder.typicode.com/todos/1"

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
url = "https://jsonplaceholder.typicode.com/posts/1"
data = {
    "userId": 10,
    "id": 10,
    "title": "Updated Title ..",
    "body": "Updated bar",
    "completed": True
}
response = requests.put(url, json = data)
print(response.status_code)
print(response.json())
