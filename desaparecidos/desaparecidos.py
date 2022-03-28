from common.settings import forum_credentials
from handlers import forum_handler as fc

username = forum_credentials['username']
password = forum_credentials['password']


def main():
    if username == "" or password == "":
        raise ValueError("Missing forum credentials! Please enter them in the 'settings.cfg' file.")

    fc.login(username, password)


if __name__ == "__main__":
    main()
