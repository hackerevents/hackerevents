#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import build
import datetime

main_folder = os.path.dirname(os.path.abspath(__file__))
event_folder = os.path.join(main_folder, 'fixtures', 'events')
partial_folder = os.path.join(main_folder, 'partials')
build_folder = os.path.join(main_folder, 'test_build')


class TestBuild(unittest.TestCase):


    def test_get_events_from_file(self):
        folder = os.path.join(event_folder, 'belgium')
        event = build.get_event_from_file(folder, '20170204-fosdem.yml')
        self.assertEqual(event['name'], "FOSDEM' 17")
        self.assertEqual(event['start'], "2017-02-04-10:00:00")
        self.assertEqual(event['end'], "2017-02-05-18:00:00")
        self.assertEqual(event['place'], 'ULB')
        self.assertEqual(event['address'],
            'Avenue Franklin Roosevelt 50 1050 Bruxelles')
        self.assertEqual(event['link'], "https://fosdem.org/")
        self.assertEqual(event['cfp'], \
            "https://fosdem.org/2017/news/2016-07-20-call-for-participation/")
        self.assertEqual(event['file_name'], '20170204-fosdem')


    def test_get_events_from_folder(self):
        base_folder = os.path.join(main_folder, 'fixtures')
        events = build.get_events_from_folder(base_folder)
        countries = events.keys()
        countries.sort()
        self.assertEqual(['belgium', 'france', 'germany'], countries)

        event = events['belgium'][0]
        self.assertEqual(event['name'], "FOSDEM' 17")
        self.assertEqual(event['start'], "2017-02-04-10:00:00")
        self.assertEqual(event['end'], "2017-02-05-18:00:00")
        self.assertEqual(event['place'], 'ULB')
        self.assertEqual(event['address'],
            'Avenue Franklin Roosevelt 50 1050 Bruxelles')
        self.assertEqual(event['link'], "https://fosdem.org/")
        self.assertEqual(event['cfp'], \
            "https://fosdem.org/2017/news/2016-07-20-call-for-participation/")
        self.assertEqual(event['file_name'], '20170204-fosdem')
        self.assertEqual(event['country'], 'belgium')


    def test_build_header(self):
        header = open(os.path.join(partial_folder, 'header.html')).read()
        self.assertEqual(build.build_header(partial_folder), header)


    def test_build_footer(self):
        header = open(os.path.join(partial_folder, 'footer.html')).read()
        self.assertEqual(build.build_footer(partial_folder), header)


    def test_write_file(self):
        build.write_file(build_folder, 'test.txt', ['test content'])
        content = open(os.path.join(build_folder, 'test.txt')).read()
        self.assertEqual('test content', content)

    def test_get_html_event(self):
        folder = os.path.join(event_folder, 'belgium')
        event = build.get_event_from_file(folder, '20170204-fosdem.yml')
        event['country'] = 'belgium'
        self.assertEqual(build.get_html_event(event), """<div class="event flex-container">
<div class="w150p">
<div class="main-date">
    <p class="day">Saturday</p>
    <p class="dayn">04</p>
    <p class="month">Feb</p>
    <p class="year">2017</p>
</div>
</div>
<div class="flex-item-fluid"><h3>FOSDEM' 17</h3>
<p class="date">From Saturday 04 February 10:00 to Sunday 05 February 18:00</p>
<p class="address">ULB<br />Avenue Franklin Roosevelt 50 1050 Bruxelles</p>
<p class=links>
<a href="https://fosdem.org/">URL</a> -
<a href="ical/belgium/20170204-fosdem.ical">ICAL</a> -
<a href="http://www.openstreetmap.org/search?query=Avenue Franklin Roosevelt 50 1050 Bruxelles">MAP</a>
<a href="https://fosdem.org/2017/news/2016-07-20-call-for-participation/"> - CFP</a>
</p></div></div>""")

    def test_build_event_list(self):

        pass

    def test_build_index_page(self):
        pass

    def test_get_ical_header(self):
        self.assertEqual(build.get_ical_header('belgium'), """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//HackerEvents//NONSGML HackerMeetups Calendar//EN
X-WR-CALNAME:Hacker Events in belgium""")

    def test_get_ical_footer(self):
        self.assertEqual(build.get_ical_footer(), 'END:VCALENDAR')

    def test_get_ical_event(self):
        folder = os.path.join(event_folder, 'belgium')
        event = build.get_event_from_file(folder, '20170204-fosdem.yml')
        event['country'] = 'belgium'
        now = datetime.datetime.now()
        self.assertEquals(build.get_ical_event(event, now), '''BEGIN:VEVENT
UID: 20170204-fosdem
DTSTAMP:%s
DTSTART:20170204T100000Z
DTEND: 20170205T180000Z
LOCATION: ULB - Avenue Franklin Roosevelt 50 1050 Bruxelles
SUMMARY:FOSDEM' 17
END:VEVENT''' % now.strftime(build.ICAL_DATE_FORMAT))

    def test_build_ical_files(self):
        pass


if __name__ == '__main__':
    unittest.main()
