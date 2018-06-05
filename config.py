import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'how_could_you_possibly_guess?'