import requests

endpoint ="https://httpbin.org/anything"

get_res = requests.get(endpoint, json={"q":"eloo"}) #http request, json/data/files interchangeable which also changes the Content-Type automatically

print(get_res.json())
print("Status Code:",get_res.status_code)
