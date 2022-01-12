import os

from fabric.connection import Connection

SUDO_USER_PROD = 'alex' #имя sudo юзера на сервере
IP_PROD = '45.147.179.67' #ip  сервера
PATH_TO_PROJECT_PROD = '/home/alex/Hype/hype' #относительный путь к папке проекта
PATH_TO_VENV_BIN_PROD = 'venv/bin/' #относительный путь к папке bin внутри вирт.окружения

DATABASE_NAME_PROD = 'hype' #навзание  базы на сервере
DATABASE_USERNAME_PROD = 'admin' #имя  пользователя bd на сервер

DATABASE_NAME_LOCAL = 'hype' #название  базы на локальной машине
DATABASE_USERNAME_LOCAL = 'admin' #имя mysql пользователя на локальной машине

PATH_TO_MEDIA_PROD = './home/alex/Hype/hype/' #путь к папке media на сервере
PATH_TO_MEDIA_LOCAL = 'hype/media' #путь к папке media на локальной машине

env = Connection()


def production_env():
    """Окружение для продакшена"""
