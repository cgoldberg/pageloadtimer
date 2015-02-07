#!/usr/bin/env python
#
# Copyright (c) 2015 Corey Goldberg
# License: MIT


import argparse
import logging
import sys
import textwrap

from pyvirtualdisplay import Display
from selenium import webdriver

logging.basicConfig(level=logging.INFO, format='%(message)s',)
logger = logging.getLogger(__name__)


def get_timings(driver):
    jscript = textwrap.dedent("""
        var performance = window.performance || {};
        var timings = performance.timing || {};
        return timings;
        """)
    all_timings = driver.execute_script(jscript)
    unused_keys = ('redirectEnd', 'redirectStart', 'toJSON',
                   'unloadEventEnd', 'unloadEventStart')
    timings = {key: all_timings[key] for key in all_timings if key not in
               unused_keys}
    return timings


def get_event_times(timings):
    ordered_events = ('navigationStart', 'fetchStart', 'domainLookupStart',
                      'domainLookupEnd', 'connectStart', 'connectEnd',
                      'secureConnectionStart', 'requestStart', 'responseStart',
                      'responseEnd', 'domLoading', 'domInteractive',
                      'domContentLoadedEventStart', 'domContentLoadedEventEnd',
                      'domComplete', 'loadEventStart', 'loadEventEnd'
                      )
    min_time = min(timings.values())
    event_times = ((event, timings[event] - min_time) for event
                   in ordered_events if event in timings)
    return event_times


def load_browser_page(url):
    logger.info('starting browser.')
    driver = webdriver.Firefox()
    logger.info('loading page.')
    driver.get(url)
    timings = get_timings(driver)
    driver.quit()
    logger.info('quitting browser.')
    event_times = get_event_times(timings)
    return event_times


class VirtualDisplay:
    def __enter__(self):
        try:
            self.xvfb_display = Display()
            self.xvfb_display.start()
        except Exception:
            print('Warning: Xvfb (virtual framebuffer) is not available.')
            print('  Using default display server instead.\n')
        return self

    def __exit__(self, *args):
        self.xvfb_display.stop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='url of page to load')
    parser.add_argument('-x', '--xvfb', action='store_true',
                        help='use xvfb virtual display')
    args = parser.parse_args()

    if not args.url.startswith('http'):
        print('URLs must start with a protocol')
        sys.exit(1)

    if args.xvfb:
        with VirtualDisplay():
            event_times = load_browser_page(url)
    else:
        event_times = load_browser_page(url)

    for event, time in event_times:
        print('{}: {:.0f}ms'.format(event, time))
