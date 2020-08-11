import sqlite3
from config import DB


def connect_to_db():
    conn = None
    try:
        conn = sqlite3.connect(DB)

    except Error as e:
        print(e)

    return conn


def get_manga_urls():
    conn = connect_to_db()
    cursor = conn.cursor()

    sql = 'SELECT manga_url FROM mangas'

    cursor.execute(sql)

    urls = cursor.fetchall()

    url_list = []
    for url in urls:
        url_list.append(url[0])

    cursor.close()
    return url_list


def add_user(user_name):
    conn = connect_to_db()
    cursor = conn.cursor()

    sql = 'INSERT INTO users (id, name) \
            VALUES (hex(randomblob(16)), "{}");'.format(user_name)

    cursor.execute(sql)
    conn.commit()
    cursor.close()


def is_manga_exists(url):
    conn = connect_to_db()
    cursor = conn.cursor()

    sql = 'SELECT manga_name FROM mangas \
            WHERE manga_url = "{}";'.format(url)

    cursor.execute(sql)

    record = cursor.fetchall()
    cursor.close()

    if len(record) != 0:
        return True
    else:
        return False


def add_manga(manga_name, manga_url, last_chapter):
    conn = connect_to_db()
    cursor = conn.cursor()

    sql = 'INSERT OR REPLACE INTO mangas (id, manga_name, manga_url, last_chapter) \
           VALUES (hex(randomblob(16)), "{}", "{}", {});'.format(manga_name,
           manga_url, last_chapter)

    cursor.execute(sql)
    conn.commit()
    cursor.close()


def update_last_chapter(manga_name, last_chapter_num):
    conn = connect_to_db()
    cursor = conn.cursor()

    sql = 'UPDATE mangas \
            SET last_chapter = {}  \
            WHERE manga_name = "{}";'.format(last_chapter_num, manga_name)

    print(sql)
    cursor.execute(sql)
    conn.commit()
    cursor.close()


def find_user(user_name):
    """ Checks if user is registered """

    conn = connect_to_db()
    cursor = conn.cursor()

    sql = 'SELECT * FROM users WHERE name = "{}"'.format(user_name)

    cursor.execute(sql)

    rows = cursor.fetchall()
    cursor.close()

    if len(rows) != 0:
        return True
    else:
        return False


def login(user_name):
    """ Login user """
    if find_user(user_name):
        print('Welcome back again')
    else:
        print('Sorry, we do not have such user')
        register(user_name)


def register(user_name):
    """ Register new user """

    answer = str(input('Would you like to register? (Yes/no) '))
    if answer.lower() == 'yes':
        add_user(user_name)
    elif answer.lower() == 'no':
        print('Ok, goodbye')


#if __name__ == '__main__':
    # add_user('manga_checker.db', 'Conor')
    #select_all_table_values('users')
    # add_manga("a", "b", 124)
    # update_last_chapter("a", 228)
    # name = str(input('Enter your name: '))
    # login(name)
