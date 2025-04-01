'''
Here we will discuss about some packages in python.
'''

'''Requests'''

# To install requests package you can run: pip install requests

import requests
from tqdm import tqdm

get_response = requests.get("https://httpbin.org/get")

# with open("index.html", 'w') as f:
#     f.write(response.text)

# print(get_response.json())
# post_response = requests.post("https://httpbin.org/post",data={'Name': 'Ratul Pal'})
# print(post_response.status_code)

# print(post_response.json())

'''To download a file and stream'''

url = "https://download-cdn.jetbrains.com/python/pycharm-professional-2024.3.5.exe"
download_file = requests.get(url, stream= True)
totalExpectedBytes = int(download_file.headers["Content-Length"])
bytesReceived = 0
progressBar = tqdm(total=totalExpectedBytes,unit_scale=True)
with open("Pycharm.exe", "wb") as f:
    for chunk in download_file.iter_content(chunk_size=128):
        progressBar.update(bytesReceived)
        f.write(chunk)
        bytesReceived += 128
progressBar.close()

'''
# Sample API URL (replace with your actual API)
url = "https://jsonplaceholder.typicode.com/posts"

# 1. GET Request (Retrieve data)
response_get = requests.get(url)
print("GET Response:", response_get.json())

# 2. POST Request (Send data)
data = {"title": "foo", "body": "bar", "userId": 1}
response_post = requests.post(url, json=data)
print("POST Response:", response_post.json())

# 3. PUT Request (Update entire resource)
update_data = {"id": 1, "title": "updated foo", "body": "updated bar", "userId": 1}
response_put = requests.put(f"{url}/1", json=update_data)
print("PUT Response:", response_put.json())

# 4. PATCH Request (Partially update resource)
patch_data = {"title": "patched title"}
response_patch = requests.patch(f"{url}/1", json=patch_data)
print("PATCH Response:", response_patch.json())

# 5. DELETE Request (Remove resource)
response_delete = requests.delete(f"{url}/1")
print("DELETE Response:", response_delete.status_code)  # Should be 200 or 204 if successful

# 6. HEAD Request (Get headers only)
response_head = requests.head(url)
print("HEAD Response Headers:", response_head.headers)

# 7. OPTIONS Request (Check allowed methods)
response_options = requests.options(url)
print("OPTIONS Response Headers:", response_options.headers)

'''


