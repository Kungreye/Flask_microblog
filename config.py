import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'how_could_you_possibly_guess?'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') # optional, by default not used.
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') # optional, by default not used.
    ADMIN = os.environ.get('ADMIN')   # list of email addrs willing to receive error reports.
    # smtp.gmail.com: default 25, TLS 587

    LANGUAGES = ['en', 'zh']
    # Flask-Babel can accept 'zh', but cannot accept hyphen like 'zh-cn', only str like 'en_US'.
    # But, moment.locale(): Chinese(China),'zh-cn';  HK, zh-hk;  Taiwan, zh-tw.  Default: 'en' for English(US)
    
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    POSTS_PER_PAGE = 6
