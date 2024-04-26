#!/usr/bin/python3
#Python script that fetches https://alx-intranet.hbtn.io/status

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    rep = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(rep)))
    print("\t- content: {}".format(rep))
    print("\t- utf8 content: {}".format(rep.decode("utf-8")))