import platform
import urllib.request
import time

def clear():
    print(u'内容较多，显示3秒后翻页')
    time.sleep(3)
    os = platform.system();
    if (os == u'Windows'):
        os.system('cls')
    else:
        os.system('clear')

def linkBaidu():
    url = 'http://www.baidu.com'
    try:
        response = urllib.request.urlopen(url,timeout=3)
        print(response.read())
    except urllib.request.URLError:
        print(u'网络地址错误')
        exit();

    with open('./baidu.txt','wb') as fp:
        fp.write(response.read())
    print(u"获取url信息，response.geturl() \n:%s" %response.geturl())

if __name__ == '__main__':
    linkBaidu()