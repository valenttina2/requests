import requests
# get-запрос
# headers = {
#     "User-Agent": "valia"
# }
# response = requests.get('https://httpbin.org/get', headers=headers,
#                         params={"a":"b"})
#
# response.raise_for_status() #проверка на правильность работы
#
# # if response.status_code == 200:
# #     print("OK")
#
# print(response)
# print(response.text)

#post запрос
# headers = {
#     "User-Agent": "valia"
# }
# response = requests.post('https://httpbin.org/post', headers=headers,
#                         params={"a":"b"},
#                          json={'username':'valia'})
# response.raise_for_status() #проверка на правильность работы

# if response.status_code == 200:
#     print("OK")

# print(response)
# print(response.text)

# url='https://jsonplaceholder.typicode.com/posts'

# response=requests.get(url)

# response=requests.post(url, data={
#     "userId":13,
#     "title":"mypost",
#     "body" : "mypostbody"
# })


#put-запрос
url='https://jsonplaceholder.typicode.com/posts/1'
print(requests.get(url).json())

response=requests.put(url, data={
    'id':1,
    'userId':'20',
    'title':'mytitle',
    'body':'mepostbody'
})
print(response.json())