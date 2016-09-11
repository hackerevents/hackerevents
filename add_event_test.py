#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import datetime
import add_event

main_folder = os.path.dirname(os.path.abspath(__file__))
event_folder = os.path.join(main_folder, 'fixtures', 'events')


class TestAdd(unittest.TestCase):

    def test_get_file_name(self):
        start = "2016-09-08-19:00:00"
        name = add_event.get_file_name(start, "Node JS Paris")
        self.assertEquals(name, "20160908-node-js-paris")
        name = add_event.get_file_name("", "")
        self.assertEquals(name, "-")

    def test_get_file_path(self):
        path = add_event.get_file_path(
            "france", "2016-09-08-19:00:00", "Node JS Paris")

        self.assertEquals(path, "events/france/20160908-node-js-paris.yml")

    def test_get_file_content(self):
        content = add_event.get_file_content(
            "2016-09-08-19:00:00", "Node JS Paris")
        date_added = datetime.datetime.now()
        self.assertEquals(content,
"""name: Node JS Paris
start: 2016-09-08-19:00:00
end: 2016-09-08-19:00:00
added: %s
place:
address:
link:
cfp:""" % date_added.strftime(add_event.DATE_ADDED_FORMAT))

if __name__ == '__main__':
    unittest.main()
