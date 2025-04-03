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


def downloadFile(url,filename):
    download_file = requests.get(url, stream= True)

    # Get total file size
    totalExpectedBytes = int(download_file.headers.get("Content-Length", 0))
    # totalExpectedBytes = int(download_file.headers[Content-Length"])

    # Initialize progress bar
    progressBar = tqdm(total=totalExpectedBytes,unit_scale=True)

    # Download and write the file
    with open(f"{filename}.exe", "wb") as f:
        for chunk in download_file.iter_content(chunk_size=128):
            if chunk:
                f.write(chunk)
                progressBar.update(len(chunk))

    # Close progress bar
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
'''In this way you can observe multi threading:'''
from concurrent.futures import ThreadPoolExecutor

listOfURLs = ["https://download-cdn.jetbrains.com/python/pycharm-professional-2024.3.5.exe",
              "https://vscode.download.prss.microsoft.com/dbazure/download/stable/ddc367ed5c8936efe395cffeec279b04ffd7db78/VSCodeUserSetup-x64-1.98.2.exe"]
listOfFileName = ["Pycherm","VSCode"]

with ThreadPoolExecutor() as T:
    T.map(downloadFile,listOfURLs,listOfFileName)


from pathlib import Path
import os

'''On this we will learn why we perffer to use pathlib over os module'''

# Build paths inside the project like this: os.path.join(BASE_DIR, 'subdir')
BASE_DIR1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                           
# Build paths inside the project like this: BASE_DIR / 'subdir'

BASE_DIR2 = Path(__file__).resolve().parent.parent

# To check the current directory:
print(Path.cwd())

# To check all the files in current working directory:

for p in Path().iterdir():
    print(p)

myFile = Path("DSA.py")

print(myFile.suffix) # To check extention of the file.
print(myFile.stem) # To check Name of the file.

print(myFile.parent) # To check the parent directory of the file.
print(myFile.parent.parent) # To check the parent directory of the parent directory of the file.
print(myFile.absolute()) # To get the absolute path of the file.
print(myFile.exists()) # To check if the file exsists.
p = Path("..").resolve() # Parent location of the exsisting file.
print(p)
p = Path(__file__).resolve() # To get the absolute path of the current file.
print(p)



