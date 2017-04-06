#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import re
import datetime


DATE_ADDED_FORMAT = "%Y-%m-%d-%H:%M:00"


def get_file_name(start, name):
    prefix = start[:10].replace('-', '')
    slug = name.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    slug = re.sub(r'[-]+', '-', slug)

    return "%s-%s" % (prefix, slug)


def get_file_path(country, start, name):
    return "events/%s/%s.yml" % (country, get_file_name(start, name))


def get_file_content(start, name):
    date_added = datetime.datetime.now()
    return """name: %s
start: %s
end: %s
added: %s
place:
address:
link:
cfp:""" % (name, start, start, date_added.strftime(DATE_ADDED_FORMAT))


def build_event_file(countr, start, name):
    file_path = get_file_path(country, start, name)
    content = get_file_content(start, name)

    event_file = open(file_path, "w")
    event_file.write(content)
    event_file.close()

    return file_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--name', metavar='name',
                        help='Name of the events.')
    parser.add_argument('--start', metavar='start',
                        help='Start date of the events.')
    parser.add_argument('--country', metavar='country',
                        help='Country where the event occurs.')
    args = parser.parse_args()

    if args.name is None:
        print("Name argument is missing")

    elif args.start is None:
        print("Start argument is missing")

    elif args.country is None:
        print("Country argument is missing")

    else:
        name = args.name
        start = args.start
        country = args.country
        file_path = build_event_file(country, start, name)

        print(file_path)
