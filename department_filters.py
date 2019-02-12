import autofilter.google_api as google
import autofilter.create_label as labels
import autofilter.create_filter as filters
import autofilter.group_manager as groups
import argparse
import time


def main():
    args = getArgs()
    try:
        labels.addLabels(google, args.show)
        filters.create_filter(google, args.show)
        print("All done. This script will close in 10 seconds. Thank you for playing Wing Commander!")
    except KeyError:
        print("Correct usage: department_filters.py -s --show.")
        print("This script will close in 10 seconds. Thank you for playing Wing Commander!")
    time.sleep(10)
    return 0


def getArgs():
    parser = argparse.ArgumentParser(
        description='Get arguments for show and group to add user to.')
    parser.add_argument('-s', '--show', type=str,
                        help='show')
    # parser.add_argument('-g', '--group', type=str,
    #                     help='group')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
