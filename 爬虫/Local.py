# coding=utf-8
from bs4 import BeautifulSoup
import requests
import re


# 获取博客文章数量
def get_page_size(user_name):
    article_list_url = 'https://blog.csdn.net/' + user_name
    req = requests.get(url=article_list_url)
    article_list_html = req.text
    bf = BeautifulSoup(article_list_html)
    page_list = bf.find('span', class_='count')
    page_size = int(page_list.text)
    if page_size % 20 > 0:
        page_size = (page_size // 20 + 1)
    else:
        page_size = page_size // 20 + 0
    return page_size

# 获取博客文章的url
def get_article_list(user_name):
    article_list_page = get_page_size(user_name)
    article_list = {}
    page_num = 1
    while page_num <= article_list_page:
        article_list_url = 'https://blog.csdn.net/' + user_name + '/article/list/' + str(page_num)
        page_num += 1
        req = requests.get(url=article_list_url)
        article_list_html = req.text
        print(article_list_html)
        bf = BeautifulSoup(article_list_html)
        print("================================="+bf)
        article_list_texts = bf.find('div', class_='article-list').find_all('h4')
        # 获取博客的地址
        for article_url in article_list_texts:
            name = article_url.find('a').text.replace(' ', '').replace('\n', '').replace('原', '').replace('转', '')
            url = article_url.find('a').get("href")
            # article_list.append(url)
            article_list[name] = url
    return article_list

if __name__ == "__main__":
    url_list = get_article_list('mydo')
    for article_name in url_list.keys():
        url = url_list[article_name]
        print(article_name)
        print(url)
        req = requests.get(url)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_='htmledit_views')
        # 判断文章是否存在
        if texts.__len__() != 0:
            # 截取文章url中的文章id，生成文件名，文件类型为。txt
            filename = re.search(r'details/[0-9]+', url).group().replace('details/', '') + '.txt'
            print(filename)
            with open(filename, 'a', encoding='utf-8') as f:
                f.writelines(article_name)
                f.write('\n\n')
                # 循环打印文章的每一行内容
                for content in texts[0].contents:
                    # 判断该行的内容是否存在
                    if content != '\n' and content != ' ':
                        text = content.find('img')
                        # 判断该行是否是img，如果是则查找并打印图片链接。否则直接打印文本内容。
                        if text != None:
                            print("image--> " + text['src'])
                            f.writelines("image--> " + text['src'])
                            f.write('\n\n')
                        else:
                            print(content.text)
                            f.writelines(content.text)
                            f.write('\n\n')
            print('--------------------')
        else:
            print("该页面不存在")
            print('--------------------')

