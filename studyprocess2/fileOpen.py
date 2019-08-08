import requests

response=requests.get("https://www.baidu.com/img/baidu_jgylogo3.gif")
print(response.content)
with open("/Users/garona/PycharmProjects/test.gif","wb") as f:
    f.write(response.content)
    f.close()
