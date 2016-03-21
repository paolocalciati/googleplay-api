##
## Basic script to retrieve the public details of an app.
## author: Alessandra Gorla
##

#!/usr/bin/python

#!/usr/bin/python

# Do not remove
GOOGLE_LOGIN = GOOGLE_PASSWORD = AUTH_TOKEN = None

import sys
import requests
from pprint import pprint

from config import *
from googleplay import GooglePlayAPI
from helpers import sizeof_fmt, print_header_line, print_result_line
from google.protobuf import text_format
from requests.packages.urllib3.exceptions import InsecureRequestWarning

if (len(sys.argv) < 2):
     print "\nUsage: %s appPackageName." % sys.argv[0]
     print "Retrieves the details (i.e. description, URL to screenshots etc) of a specific app.\n"
     sys.exit(0)

# Dealing with user's parameter
appname = sys.argv[1]

# Ignore unverified HTTPS request warning.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# authentication
api = GooglePlayAPI(ANDROID_ID)
api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)

#invoking api method to get the app details.
detailsResponse = api.details(appname)
print text_format.MessageToString(detailsResponse)


