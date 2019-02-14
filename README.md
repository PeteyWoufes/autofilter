# Autofilter
A utility for programatically creating and adding labels, filters and groups using the Gmail API.

## Installation

To use this program you will need to provide a few things:
* A P12 Google service account keyfile, which you can get at https://console.cloud.google.com/.
* A Google service account email and password, which you can get at https://console.developers.google.com/iam-admin/serviceaccounts.
* Authorization to use the scopes specified in the auth_template file, which you will need to be authorized for by your G Suite Administrator. You will need to remove the "_template" and configure the file with your credentials.
* Filters and labels to create, which are listed in the config file. A template is provided. 
* Groups to create and users to add to those groups.

To work with the source code provided you will also need to install some modules. You can do this by entering the following command into your Python interpreter:
```Python
pip install -r requirements.txt
```

## Usage
The Autofilter library contains (as of 14th of February 2018):
* create_filter, a script for creating and adding filters and filter objects.
* create_label, a script for creating labels, one at a time or in bulk.
* fetch_label_ids, a script which only contains one method; this script checks what labels exist on a user's Gmail account and provide you with names and IDs for them.
* google_api, a script which generates Service Account Credentials to use for impersonating Gmail users, and creates services to access the Gmail and Directory APIs.
* group_manager, a script for creating and listing groups and users.

Of those scripts, you should use all but google_api, because google_api is only used internally by the other scripts. 

## License
This program is licenced under the MIT License. In short, all I require is that you preserve the copyright and license notices in this code. You can do whatever you want with it and you are not obligated to publish your improvements upstream, however, it would be greatly appreciated!