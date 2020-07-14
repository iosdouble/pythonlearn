from fake_useragent import UserAgent

ua = UserAgent()
print(ua.ie)     #ie的 内核
print(ua.chrome) #谷歌浏览器 内核

useragent = ua.random  ##随机选取一个浏览器内核
headers = {'User-Agent': useragent}
print(headers)

