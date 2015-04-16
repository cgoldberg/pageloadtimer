#!/usr/bin/env python
#
# Copyright (c) 2015 Corey Goldberg
# License: MIT


import logging
import textwrap

from pyvirtualdisplay import Display
from selenium import webdriver

logging.basicConfig(level=logging.INFO, format='%(message)s',)
logger = logging.getLogger(__name__)


class PageLoadTimer:

    def __init__(self, driver):
        self.driver = driver


    def _execute_timing_js(self):
        jscript = textwrap.dedent("""
            var performance = window.performance || {};
            var timings = performance.timing || {};
            return timings;
            """)
        timings = self.driver.execute_script(jscript)
        return timings


    def get_event_times(self):
        ordered_events = ('navigationStart', 'fetchStart', 'domainLookupStart',
                          'domainLookupEnd', 'connectStart', 'connectEnd',
                          'secureConnectionStart', 'requestStart', 'responseStart',
                          'responseEnd', 'domLoading', 'domInteractive',
                          'domContentLoadedEventStart', 'domContentLoadedEventEnd',
                          'domComplete', 'loadEventStart', 'loadEventEnd'
                          )
        timings = self._execute_timing_js()
        min_time = min((epoch for epoch in timings.values() if epoch != 0))
        event_times = ([(event, timings[event] - min_time) for event
                       in ordered_events if event in timings])
        return event_times



if __name__ == '__main__':
        url = 'http://www.google.com'
        driver = webdriver.Firefox()
        driver.get(url)
        timer = PageLoadTimer(driver)
        print timer.get_event_times()
        driver.quit()
