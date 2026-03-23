
import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data[0]["title"])  # print only title
    else:
        print("Error:", response.status_code)

except Exception as e:
    print("Something went wrong:", e)
