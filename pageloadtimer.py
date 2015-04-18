#!/usr/bin/env python
#
# Copyright (c) 2015 Corey Goldberg
# License: MIT


import collections
import logging
import textwrap

from pyvirtualdisplay import Display
from selenium import webdriver


class PageLoadTimer:

    def __init__(self, driver):
        self.driver = driver

        self.jscript = textwrap.dedent("""
            var performance = window.performance || {};
            var timings = performance.timing || {};
            return timings;
            """)


    def inject_timing_js(self):
        timings = self.driver.execute_script(self.jscript)
        return timings


    def get_event_times(self):
        ordered_events = ('navigationStart', 'fetchStart', 'domainLookupStart',
                          'domainLookupEnd', 'connectStart', 'connectEnd',
                          'secureConnectionStart', 'requestStart', 'responseStart',
                          'responseEnd', 'domLoading', 'domInteractive',
                          'domContentLoadedEventStart', 'domContentLoadedEventEnd',
                          'domComplete', 'loadEventStart', 'loadEventEnd'
                          )
        timings = self.inject_timing_js()
        min_time = min((epoch for epoch in timings.values() if epoch != 0))
        event_times = ([(event, timings[event] - min_time) for event
                       in ordered_events if event in timings])
        event_times_ordered = collections.OrderedDict(event_times)
        return event_times_ordered



if __name__ == '__main__':
    url = 'http://www.example.com'
    driver = webdriver.Firefox()
    driver.get(url)
    timer = PageLoadTimer(driver)
    print timer.get_event_times()
    driver.quit()
