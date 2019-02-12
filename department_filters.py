import autofilter.google_api as google
import autofilter.create_label as labels
import autofilter.create_filter as filters
import autofilter.group_manager as groups
import argparse


def main():
    args = getArgs()
    filters.create_filter(google, args.show)


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
