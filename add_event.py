#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import re


def get_file_name(start, name):
    prefix = start[:10].replace('-', '')
    slug = name.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    slug = re.sub(r'[-]+', '-', slug)

    return "%s-%s" % (prefix, slug)


def get_file_path(country, start, name):
    return "events/%s/%s.yml" % (country, get_file_name(start, name))


def get_file_content(start, name):
    return """name: %s
start: %s
end: %s
place:
address:
link:
cfp:""" % (name, start, start)


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
        print "Name argument is missing"

    elif args.start is None:
        print "Start argument is missing"

    elif args.country is None:
        print "Country argument is missing"

    else:
        name = args.name
        start = args.start
        Path = get_file_path(country, start, name)
        content =  get_file_content(start, name)

        event_file = open(path, "w")
        event_file.write(content)
        event_file.close()

        print "File created at path:"
        print path

