#!/usr/bin/python3
import requests
import command
import sys

from bs4 import BeautifulSoup

response = requests.get(command.url, params=command.attr)
data = response.json()

try:
    if command.args.min:
        print("\n")
        print('*' * 100)
    for attr in data['data']['movies']:
        if not command.args.min:
            print("\n")
            print('*' * 100)
            print("Movie Title     :", attr['title_english'])
            print("Year Released   :", attr['year'])
            print("Genre           :", attr['genres'])
            print("MPAA Rating     :", attr['mpa_rating'])
            for qual in attr['torrents']:
                if qual['quality'] == command.attr['quality']:
                    print("Torrent quality :", qual['quality'])
                    print("Torrent size    :", qual['size'])
                    print("Torrent URL     :", qual['url'])
            print('*' * 100)
        else:
            print("\n")
            print("Movie Title     :", attr['title_english'])
            for qual in attr['torrents']:
                if qual['quality'] == command.attr['quality']:
                    print("Torrent URL     :", qual['url'])

    if command.args.min:
        print("\n")
        print('*' * 100)
except:
    print("\nNot found\n")

sys.stdout.logend()
