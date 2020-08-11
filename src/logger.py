import logging

def set_basic_config():
    logging.basicConfig(
            level=logging.INFO, 
            filename='../Logs/db.log', 
            filemode='a', 
            format='%(asctime)s - %(message)s',
            datefmt='%d.%M.%Y %H:%M:%S'
            )


def user_logged(user_name):
    logging.info(f'{user_name} logged in')


def added_new_manga(manga_name):
    logging.info(f'{manga_name} added in db')


#if __name__ == '__main__':
#    set_basic_config()
#    user_logged('Conor')
