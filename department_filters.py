import autofilter.google_api
import autofilter.create_label
import autofilter.create_filter
import autofilter.group_manager
import argparse


def main():
    args = getArgs()


def getArgs():
    parser = argparse.ArgumentParser(description='Get arguments for show and group to add user to.')
    parser.add_argument('-s', '--show', type=str,
                        help='show')
    parser.add_argument('-g', '--group', type=str,
                        help='group')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
