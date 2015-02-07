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

  - pyvirtualdisplay
  - selenium

----

**Installation from GitHub repo**

1. Install system requirements (Debian/Ubuntu)::

    $ sudo apt-get install -y firefox git python-virtualenv xvfb

2. Clone the pageloadtimer repo::

    $ git clone https://github.com/cgoldberg/pageloadtimer.git
    $ cd pageloadtimer

3. create and activate a virtualenv::

    $ virtualenv env
    $ source env/bin/activate

4. Install pageloadtimer and requirements::

    $ pip install -e .

----

**Usage**

- load a page and get timing info::

    $ python pageloadtimer.py http://example.com

- load a page with the browser inside a virtual display server (headless)::

    $ python pageloadtimer.py -x http://example.com

----

**Further Reading**:

- Navigation Timing API: `W3C Recommendation <http://www.w3.org/TR/navigation-timing/>`_
- Navigation Timing API: `Mozilla Developer Network <https://developer.mozilla.org/en-US/docs/Navigation_timing>`_
- Selenium WebDriver: `PyPI <https://pypi.python.org/pypi/selenium>`_

----

**Browser Processing Model**:

.. image:: timing-overview.png
