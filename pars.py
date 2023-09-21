import requests
from bs4 import BeautifulSoup as B


# HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
url = 'https://kaktus.media/?lable=8&date=2023-09-21&order=time'


def get_html(url):
    response = requests.get(url)
    return response.text


def get_soup(html):
    soup = B(html, 'lxml')
    return soup



def get_date(url):
    html = get_html(url)
    soup = get_soup(html)
    return soup.find('span', class_='PaginatorDate--today-text').text.strip()

def get_data(soup):
    news = soup.find_all('div', class_='ArticleItem--data') 
    
    newspaper = []
    for new in news:
        try:
            title = new.find('a', class_='ArticleItem--name').text.strip()
        except:
            title = ''

        try:
            link = new.find('a', class_='ArticleItem--name').get('href')
        except:
            link = ''
        paper = {title: link}
        print()
        newspaper.append(paper)
    
    return newspaper


def main(url):
    html = get_html(url)
    soup = get_soup(html)
    return get_data(soup)

