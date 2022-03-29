import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--post', action='store_true')
    arguments = parser.parse_args()
    return arguments


arguments = parse_arguments()
