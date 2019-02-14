import autofilter.google_api as google
import autofilter.create_label as af_labels
import autofilter.create_filter as filters
import autofilter.group_manager as groups
import autofilter.fetch_label_ids as fetch_labels
import json


def main():
    ''' Loads config data. '''
    data = loadData()
    try:
        for user in data["users"]:
            ''' Creates single label for a user. '''
            af_labels.add(user, "Pipeline")
            ''' Gets existing labels for user's Gmail account. '''
            labels = fetch_labels.fetch_labels(google, user)
            ''' Creates filter object using criteria provided by you, labels fetched earlier and a label name. '''
            obj = filters.create_filter_object(
                {"from": "pipeLine@giant.ie"}, labels, "Pipeline")
            ''' Adds filter to the user's Gmail account. '''
            filters.add(user, obj)
        print("All done.")
    except:
        print("ERROR.")


def loadData():
    ''' Loads config file. '''
    with open("config.json", "r") as x:
        data = json.loads(x.read())
    return data


if __name__ == "__main__":
    main()
