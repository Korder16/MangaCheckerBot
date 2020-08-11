import checker
import db_client
import logger


def add_new_manga(url):
    """ New manga adds into db """

    manga_name = checker.get_manga_name_by_url(url)
    last_chapter = checker.get_last_chapter(url)

    if not db_client.is_manga_exists(url):
        db_client.add_manga(manga_name, url, last_chapter)
        logger.added_new_manga(manga_name)


def check_for_new_chapters():
    url_list = db_client.get_manga_urls()
    for url in url_list:
        print(checker.get_manga_name_by_url(url),
                checker.get_last_chapter(url))




if __name__ == '__main__':
    logger.set_basic_config()
#    urls = ['https://readmanga.live/tales_of_demons_and_gods',
#            'https://readmanga.live/my_hero_academia__A1be6f8']

#    for url in urls:
#        add_new_manga(url)
    check_for_new_chapters()
