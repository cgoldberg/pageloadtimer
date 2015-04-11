#!/usr/bin/env python
#
# Copyright (c) 2015 Corey Goldberg
# License: MIT


import argparse
import logging
import textwrap

from pyvirtualdisplay import Display
from selenium import webdriver

logging.basicConfig(level=logging.INFO, format='%(message)s',)
logger = logging.getLogger(__name__)


def execute_timing_js(driver):
    jscript = textwrap.dedent("""
        var performance = window.performance || {};
        var timings = performance.timing || {};
        return timings;
        """)
    timings = driver.execute_script(jscript)
    return timings


def get_event_times(timings):
    ordered_events = ('navigationStart', 'fetchStart', 'domainLookupStart',
                      'domainLookupEnd', 'connectStart', 'connectEnd',
                      'secureConnectionStart', 'requestStart', 'responseStart',
                      'responseEnd', 'domLoading', 'domInteractive',
                      'domContentLoadedEventStart', 'domContentLoadedEventEnd',
                      'domComplete', 'loadEventStart', 'loadEventEnd'
                      )
    min_time = min((epoch for epoch in timings.values() if epoch != 0))
    event_times = ((event, timings[event] - min_time) for event
                   in ordered_events if event in timings)
    return event_times


def load_browser_page(url):
    driver = webdriver.Firefox()
    driver.get(url)
    timings = execute_timing_js(driver)
    driver.quit()
    event_times = get_event_times(timings)
    return event_times


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='url of page to load')
    parser.add_argument('-r', '--repeat', action='store', default=1, metavar='N', type=int, nargs='?', help='run N times')
    parser.add_argument('-x', '--xvfb', action='store_true', help='use xvfb virtual display')
    args = parser.parse_args()

    if args.url.startswith('http'):
        url = args.url
    else:
        url = 'http://{}'.format(args.url)

    if args.xvfb:
        xvfb_display = Display()
        xvfb_display.start()

    for _ in range(args.repeat):
        event_times = load_browser_page(url)

        logger.info('\n')
        logger.info('navigation event timings:')
        logger.info('*************************')

        for event, time in event_times:
            logger.info('{}: {:.0f}ms'.format(event, time))

    if args.xvfb:
        xvfb_display.stop()
