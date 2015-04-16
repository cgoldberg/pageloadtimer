import unittest

from selenium import webdriver

import pageloadtimer


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.addCleanup(self.driver.quit)

        self.results = [
            ('navigationStart', 0), ('fetchStart', 96), ('domainLookupStart', 96),
            ('domainLookupEnd', 96), ('connectStart', 96), ('connectEnd', 96),
            ('requestStart', 258), ('responseStart', 366), ('responseEnd', 409),
            ('domLoading', 366), ('domInteractive', 438),
            ('domContentLoadedEventStart', 444), ('domContentLoadedEventEnd', 449),
            ('domComplete', 889), ('loadEventStart', 889), ('loadEventEnd', 891)
        ]


    def test_fields(self):
        self.driver.get('http://www.example.com')
        self.assertEqual(self.driver.title, 'Example Domain')
        plt = pageloadtimer.PageLoadTimer(self.driver)
        expected = [x[0] for x in self.results]
        actual = [x[0] for x in plt.get_event_times()]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
