import configparser
import pathlib

SETTINGS_FILEPATH = pathlib.Path(__file__).parents[2].resolve().joinpath('settings.cfg')


def load_settings():
    settings = configparser.RawConfigParser()
    settings.read(SETTINGS_FILEPATH)
    return settings


settings = load_settings()
forum_credentials = dict(settings.items('FORUM_CREDENTIALS'))
