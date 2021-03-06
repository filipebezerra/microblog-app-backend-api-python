import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'dev-microblog-sec-key'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        f'sqlite:///{os.path.join(basedir, "app.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    ADMINS = ['filipebzerra@gmail.com']
    POSTS_PER_PAGE = os.getenv('POSTS_PER_PAGE') or 10
    PASSWORD_RESET_EXPIRES_AT = os.getenv('PASSWORD_RESET_EXPIRES_AT') or 600
    DATE_TIME_FORMAT = os.getenv('DATE_TIME_FORMAT') or '%Y-%m-%dT%H:%M:%S,%f'
    LANGUAGES = ['en_US', 'es', 'pt_BR']
    MS_TRANSLATOR_KEY = os.getenv('MS_TRANSLATOR_KEY')
    MS_TRANSLATOR_REGION = os.getenv('MS_TRANSLATOR_REGION')
    ELASTICSEARCH_URL = os.getenv('ELASTICSEARCH_URL')
    LOG_TO_STDOUT = os.getenv('LOG_TO_STDOUT')
    REDIS_URL = os.getenv('REDIS_URL') or 'redis://'
    MICROBLOG_QUEUE_NAME = os.getenv('MICROBLOG_QUEUE_NAME') or \
        'microblog-tasks'
    ITEMS_PER_REQUEST = os.getenv('ITEMS_PER_PAGE') or 10
    MAX_RESULTS_PER_REQUEST = os.getenv('MAX_RESULTS_PER_REQUEST') or 100


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
