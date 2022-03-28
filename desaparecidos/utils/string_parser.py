import re


def get_post_id(post_url):
    return re.findall(r'\d+', post_url)[-1]
