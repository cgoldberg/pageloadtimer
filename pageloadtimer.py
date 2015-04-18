#!/usr/bin/env python
#
# Copyright (c) 2015 Corey Goldberg
# License: MIT


import collections
import textwrap

from selenium import webdriver


class PageLoadTimer:

    def __init__(self, driver):
        """
            takes:
                driver: webdriver instance from selenium package.
            this should be instantiated with an active driver.
        """
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
        timings = self.inject_timing_js()
        # the W3C Navigation Timing spec guarantees a monotonic clock:
        #  "The difference between any two chronologically recorded timing
        #   attributes must never be negative. For all navigations, including
        #   subdocument navigations, the user agent must record the system
        #   clock at the beginning of the root document navigation and define
        #   subsequent timing attributes in terms of a monotonic clock
        #   measuring time elapsed from the beginning of the navigation."
        # However, some navigation events produce a value of 0 when unable to
        # retrieve a timestamp.  We filter those out here:
        good_values = [epoch for epoch in timings.values() if epoch != 0]
        # rather than time since epoch, we care about elapsed time since first
        # sample was reported until event time.  Since the dict we received was
        # inherently unordered, we order things here, according to W3C spec
        # fields.
        ordered_events = ('navigationStart', 'fetchStart', 'domainLookupStart',
                          'domainLookupEnd', 'connectStart', 'connectEnd',
                          'secureConnectionStart', 'requestStart',
                          'responseStart', 'responseEnd', 'domLoading',
                          'domInteractive', 'domContentLoadedEventStart',
                          'domContentLoadedEventEnd', 'domComplete',
                          'loadEventStart', 'loadEventEnd'
                          )
        event_times = ((event, timings[event] - min(good_values)) for event
                       in ordered_events if event in timings)
        return collections.OrderedDict(event_times)


if __name__ == '__main__':
    url = 'http://www.example.com'
    driver = webdriver.Firefox()
    driver.get(url)
    timer = PageLoadTimer(driver)
    print timer.get_event_times()
    driver.quit()
