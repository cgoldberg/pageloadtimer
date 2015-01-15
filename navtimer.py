#!/usr/bin/env python
#
# Copyright (c) 2015 Corey Goldberg
# License: MIT


from pprint import pprint
import textwrap

import easyprocess
from pyvirtualdisplay import Display
from selenium import webdriver


def get_timings(driver):
    jscript = textwrap.dedent("""
        var performance = window.performance || {};
        var timings = performance.timing || {};
        return timings;
        """)
    timings = driver.execute_script(jscript)
    unused_keys = ('toJSON', 'unloadEventEnd', 'unloadEventStart')
    timings = {key: timings[key] for key in timings if key not in unused_keys}
    return timings


def get_event_times(timings):
    ordered_events = ('navigationStart', 'redirectStart', 'redirectEnd',
                      'fetchStart', 'domainLookupStart', 'domainLookupEnd',
                      'connectStart', 'connectEnd', 'secureConnectionStart',
                      'requestStart', 'responseStart', 'responseEnd',
                      'domLoading', 'domInteractive',
                      'domContentLoadedEventStart', 'domContentLoadedEventEnd',
                      'domComplete', 'loadEventStart', 'loadEventEnd'
                      )
    min_time = min(timings.values())
    event_times = [(event, timings[event] - min_time) for event
                   in ordered_events if event in timings]
    return event_times


def load_page(url, virtual_display=True):
    if virtual_display:
        try:
            xvfb_display = Display()
            xvfb_display.start()
        except easyprocess.EasyProcessCheckInstalledError:
            print('Warning: virtual framebuffer is not available.')
            print('  please install Xvfb.')
            print('  running in regular display server.\n')
            virtual_display = False
    driver = webdriver.Firefox()
    driver.get(url)
    timings = get_timings(driver)
    driver.quit()
    if virtual_display:
        xvfb_display.stop()
    event_times = get_event_times(timings)
    return event_times


if __name__ == '__main__':
    url = 'https://www.example.org/'
    event_times = load_page(url)
    pprint(event_times)
