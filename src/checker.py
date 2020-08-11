import requests
import asyncio

from pprint import pprint
from bs4 import BeautifulSoup
from manga_list import MANGA_DICT

def get_page(url):
    """ Get page by request """

    page = requests.get(url)
    return page


def parse_page(page, css_selector):
    """ Parse html page to find number of current manga """

    soup = BeautifulSoup(page.text, 'html.parser')
    chapter = soup.select(css_selector)
    return chapter  


def get_last_chapter(url):
    """ Return last manga chapter """

    page = get_page(url)
    css_selector = 'h4 > a[href*="/vol"]'
    last_chapter_str = parse_page(page, css_selector)[0].get_text().split(' - ')[-1]
    last_chapter = last_chapter_str.split(' ')[0]
    return last_chapter

    

def check_updates():
    """ Checks updates for all mangas in list """

    for manga_name in MANGA_DICT.keys():
        print(manga_name, get_last_chapter(manga_name))


def get_manga_name_by_url(url):
    """ Returns manga name by url """

    page = get_page(url)
    css_selector = 'span.name'
    manga_name = parse_page(page, css_selector)[0].get_text()
    return manga_name


#if __name__ == '__main__':
#    check_updates()
#    print(get_manga_name_by_url('https://readmanga.live/one_punch_man__A1bc88e'))

