
import autofilter.google_api as google
import autofilter.create_label as labels
import autofilter.create_filter as filters
import autofilter.group_manager as groups
import autofilter.fetch_label_ids as fetch_labels
import json
import argparse


def main():
    data = loadData()
    try:
        for user in data["users"]:
            labels = fetch_labels.fetch_labels(google, user)
            filters.replace_names(labels, "test1")
        print("All done.")
    except KeyError:
        print(KeyError)


def loadData():
    with open("config.json", "r") as x:
        data = json.loads(x.read())
    return data


'''
def getArgs():
    parser = argparse.ArgumentParser(
        description='Get arguments for show and group to add user to.')
    parser.add_argument('-s', '--show', type=str,
                        help='show')
    # parser.add_argument('-g', '--group', type=str,
    #                     help='group')
    args = parser.parse_args()
    return args
'''

if __name__ == "__main__":
    main()
