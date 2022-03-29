from common.settings import forum_credentials

from handlers import forum_handler as fc
from common import routines as rt

username = forum_credentials['username']
password = forum_credentials['password']


def main():
    if username == "" or password == "":
        raise ValueError("Missing forum credentials! Please enter them in the 'settings.cfg' file.")

    fc.login(username, password)

    while True:
        rt.check_directory()
        rt.check_monitored_persons()


if __name__ == "__main__":
    main()
