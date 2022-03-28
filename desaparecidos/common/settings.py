import configparser

SETTINGS_FILEPATH = '../settings.cfg'


def load_settings():
    settings = configparser.RawConfigParser()
    settings.read(SETTINGS_FILEPATH)
    return settings


settings = load_settings()
forum_credentials = dict(settings.items('FORUM_CREDENTIALS'))
