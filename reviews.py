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
     print "\nUsage: %s appPackageName [maxNumReviews]" % sys.argv[0]
     print "Retrieves the reviews of a specific app. It retrieves the " \
         "[maxNumReviews] most recent reviews. This number is anyhow limited to " \
         "500, which is also the default value. \n"
     sys.exit(0)


# Dealing with user's parameter
appname = sys.argv[1]
if (len(sys.argv) == 3):
    maxNumReviews = int(sys.argv[2])
    # if specified value is >500, set it to 500 (maximum value).
    if maxNumReviews > 500:
        maxNumReviews = 500
# if not specified, set the number of reviews to 500 (default value).
else:
    maxNumReviews = 500


# ingore unverified HTTPS request warning.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# authentication
api = GooglePlayAPI(ANDROID_ID)
api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)

# Each request returns 20 reviews.
# Loop until you find no more or reach the limit of 500
for offsetNum in range(0, maxNumReviews, 20):
    reviewResponse = api.reviews(appname, offset=offsetNum)
    print text_format.MessageToString(reviewResponse.getResponse)
    # if nextPageUrl is not present in response, there are no reviews left 
    if not reviewResponse.nextPageUrl:
        break


