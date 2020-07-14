import requests
import bs4
import re
import logging
import threading
import time


# 获取每页中的每组图片网页
def execute_downinfo(second_href):
    time.sleep(0.1)
    rr = requests.get(second_href)
    exampleSoupp = bs4.BeautifulSoup(rr.content, 'html5lib')
    elemss = exampleSoupp.select(".wp-list li a")
    for elemm in elemss:
        get_downloadinfo(elemm['href'])


# 获得日志对象
def get_logger():
    logger = logging.getLogger()
    fileHandler = logging.FileHandler('./meizi.log', mode='a', encoding='UTF-8')
    logger.setLevel(logging.INFO)
    logger.addHandler(fileHandler)
    return logger


# 获得每张图片的地址
def get_downloadinfo(third_url):
    try:
        time.sleep(0.1)
        r = requests.get(third_url)
        exampleSoup = bs4.BeautifulSoup(r.content, 'html5lib')
        elems = exampleSoup.select("#maincontent img")
        srcs = []
        names = []
        for elem in elems:
            tmp = str(elem["src"]).split("/")
            tmpp = tmp[5] + "-" + tmp[6] + "-" + tmp[7] + "-" + tmp[8]
            names.append(tmpp)
            srcs.append(elem["src"])
        c = dict(zip(srcs, names))
        for key in c.keys():
            tmp = []
            tmp.append(key)
            tmp.append(c.get(key))
            time.sleep(0.1)
            download_img(tmp)
    except Exception as ex:
        print("get_downloadinfo")
        print(ex)
        print("--------error contine----")
        pass


# 下载图片
def download_img(url_info):
    if url_info[1]:
        try:
            # print("-----------downloading %s"%(url_info[0]))
            url = url_info[0]
            time.sleep(0.1)
            response = requests.get(url)
            if response.status_code != requests.codes.ok:
                return
            img = response.content
            path = './meizi/%s' % (url_info[1])
            with open(path, 'wb') as f:
                f.write(img)
        except Exception as ex:
            print("download_img ")
            print(ex)
            print("--------error contine----")
            pass


# 拉取总页数并启用多线程分别下载每页的内容
def getSecondpage(url):
    try:
        pattern = re.compile(r'\d+')
        '''
        header = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Cache-Control":"no-cache",
            "Connection":"keep-alive",
            "Pragma":"no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
            "Content-Type": "text/html"
        }
        '''
        r = requests.get(url)
        print(r.content)
        time.sleep(3)
        exampleSoup = bs4.BeautifulSoup(r.content, 'html5lib')
        elems = exampleSoup.select("#wp_page_numbers ul li a")
        lastindex = int(pattern.findall(elems[len(elems) - 1]['href'])[0])
        second_hrefs = []
        for i in range(1, lastindex + 1):
            second_hrefs.append("http://www.meizitu.com/a/more_" + str(i) + ".html")
        # second_hrefs = second_hrefs[len(second_hrefs)-2:]
        for second_href in second_hrefs:
            arg = second_href
            threading.Thread(target=execute_downinfo, args=(arg,)).start()
    except Exception as ex:
        print("getSecondpage")
        print(ex)
        print("--------error contine----")
        pass


# 主函数入口
if __name__ == '__main__':
    logger = get_logger()
    logger.info("App start")
    url = "http://www.meizitu.com/"
    getSecondpage(url)

