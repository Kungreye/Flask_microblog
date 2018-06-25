import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'how_could_you_possibly_guess?'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') # optional, by default not used.
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') # optional, by default not used.
    ADMINS = ['kungreye@gmail.com']    # list of email addrs willing to receive error reports.
    # smtp.gmail.com: default 25, TLS 587

    LANGUAGES = ['en', 'zh_CN', 'zh']
    # Flask-Babel cannot accept hyphen like zh-cn, only str like 'en_US'; so modified to zh_CN
    # yet moment.locale() required:  Chinese(China),'zh-cn';  HK, zh-hk;  Taiwan, zh-tw.  Default: 'en' for English(US)
    
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')     # Azure subscription key is exported in env variable.
    
    POSTS_PER_PAGE = 3