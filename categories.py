#!/usr/bin/python

# Do not remove
GOOGLE_LOGIN = GOOGLE_PASSWORD = AUTH_TOKEN = None

import requests
import sys
import urlparse
from pprint import pprint
from google.protobuf import text_format

from config import *
from googleplay import GooglePlayAPI

# Ignore unverified HTTPS request warning.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

api = GooglePlayAPI(ANDROID_ID)
api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)
response = api.browse()

print SEPARATOR.join(["ID", "Name"])
for c in response.category:
  print SEPARATOR.join(i.encode('utf8') for i in [urlparse.parse_qs(c.dataUrl)['cat'][0], c.name])

