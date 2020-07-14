# coding=utf-8
from bs4 import BeautifulSoup
import requests


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
        bf = BeautifulSoup(article_list_html)
        article_list_texts = bf.find('div', class_='article-list').find_all('h4')
        # 获取博客的地址
        for article_url in article_list_texts:
            name = article_url.find('a').text.replace(' ', '').replace('\n', '').replace('原', '').replace('转', '')
            url = article_url.find('a').get("href")
            # article_list.append(url)
            article_list[name] = url
    return article_list


if __name__ == "__main__":
    print(get_article_list('mydo'))

