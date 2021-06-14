# _*_ coding=utf8 _*_
import requests
import json
# r = requests.get("https://www.baidu.com")
# print(r.text)


params={"first_name":"hello","last_name":"word"}
# headers={"Content-Tpye":"application/json"}
headers={"Content-Tpye":"application/x-www-form-urlencoded"}
responds=requests.post("http://httpbin.org/post",data=params,headers=headers)
print(responds.text)
print(responds.url)
print(responds.text)
print(responds.url)
print(responds.request)
print(responds.request)

result=json.loads(responds.text)
print(type(result))

# params={"first_name":"hello","last_name":"word"}
# responds=requests.post("http://httpbin.org/po