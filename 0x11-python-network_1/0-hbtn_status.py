#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
"""

from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as url:
        data = url.read()
        print('Body response:')
        print(f'\t- type: {type(data)}')
        print(f'\t- content: {data}')
        print(f'\t- utf8 content: {data.decode("utf-8")}')
