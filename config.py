import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    YA_TRANSLATOR_KEY = 'trnsl.1.1.20190203T115351Z.1605d09ad9625372.06d7c4f9ca9130fcf31a1037f5b81b3788cace6a'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    ADMINS = ['your-email@example.com']
    POSTS_PER_PAGE = 25
    LANGUAGES = ['en', 'ru', 'es']

    ELASTICSEARCH_URL = 'ELASTICSEARCH_URL=http://localhost:9200'

# TODO: FUNCTIONALITY "MAIL REPORT" DOESNT'T WORK
# TODO: FUNCTIONALITY "ELASTIC SEARCH" DOESN'T WORK
