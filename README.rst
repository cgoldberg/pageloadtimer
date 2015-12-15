-------------
pageloadtimer
-------------

**Automated Page Load Timer - Web Navigation Timing (PerformanceTiming Interface)**

- Author: Corey Goldberg, 2015
- License: MIT
- Development: `https://github.com/cgoldberg/pageloadtimer <https://github.com/cgoldberg/pageloadtimer>`_

----

**About**:

**pageloadtimer** is a Python program for timing automated browser page loads.  It uses Selenium WebDriver to drive a browser, and gathers metrics from the Navigation Timing API's `PerformanceTiming` Interface.  This allows you to measure performance for different phases of loading a web page in a Browser.

----

**Requirements**:

- Python Version:

  - Python 2.7+ or Python 3.3+

- System Dependencies:

  - Firefox (web browser)
  - Xvfb (virtual display server)

- Python Requirements:

  - selenium
  - xvfbwrapper

----

**Installation from GitHub repo**

1. install system requirements (Debian/Ubuntu)::

    $ sudo apt-get install -y firefox git python-virtualenv xvfb

2. clone the pageloadtimer repo::

    $ git clone https://github.com/cgoldberg/pageloadtimer.git
    $ cd pageloadtimer

3. create and activate a virtualenv::

    $ virtualenv env
    $ source env/bin/activate

4. install pageloadtimer and requirements::

    $ pip install -e .

----

**Usage**

- load a page and get timing info::

    $ python pageloadtimer.py http://example.com

- load a page and get timing info, with the browser running headless (Xvfb).::

    $ python pageloadtimer.py -x http://example.com

----

**Example**

::

    $ python pageloadtimer.py -x www.example.com
    starting browser.
    loading page.
    quitting browser.


    navigation event timings:
    *************************
    navigationStart: 0ms
    fetchStart: 2ms
    domainLookupStart: 2ms
    domainLookupEnd: 2ms
    connectStart: 2ms
    connectEnd: 2ms
    requestStart: 113ms
    responseStart: 154ms
    responseEnd: 155ms
    domLoading: 154ms
    domInteractive: 173ms
    domContentLoadedEventStart: 173ms
    domContentLoadedEventEnd: 173ms
    domComplete: 181ms
    loadEventStart: 181ms
    loadEventEnd: 181ms

----

**Further Reading**:

- Navigation Timing API: `W3C Recommendation <http://www.w3.org/TR/navigation-timing/>`_
- Navigation Timing API: `Mozilla Developer Network <https://developer.mozilla.org/en-US/docs/Navigation_timing>`_
- Selenium WebDriver: `PyPI <https://pypi.python.org/pypi/selenium>`_

----

**Browser Processing Model**:

.. image:: timing-overview.png
