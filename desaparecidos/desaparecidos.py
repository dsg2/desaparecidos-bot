from common.settings import forum_credentials as credentials
from common.arguments import arguments as args

from handlers import forum_handler as fc
from common import routines as rt

username = credentials['username']
password = credentials['password']


def main():
    post_mode = args.post

    if username == "" or password == "":
        raise ValueError("Missing forum credentials! Please enter them in the 'settings.cfg' file.")

    fc.login(username, password)

    if not post_mode:
        rt.check_directory(post_mode)

    while True:
        rt.check_directory(post_mode=True)
        rt.check_monitored_persons()


if __name__ == "__main__":
    main()
