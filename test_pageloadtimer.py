import unittest

from selenium import webdriver

import pageloadtimer


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.addCleanup(self.driver.quit)

    def test_upper(self):
        self.driver.get('http://www.example.com')
        self.assertEqual(self.driver.title, 'Example Domain')

    #def test_upper(self):
    #    self.assertEqual('foo'.upper(), 'FOO')

    #def test_isupper(self):
    #    self.assertTrue('FOO'.isupper())
    #    self.assertFalse('Foo'.isupper())

    #def test_split(self):
    #    # check that s.split fails when the separator is not a string
    #    with self.assertRaises(TypeError):
    #        s.split(2)

if __name__ == '__main__':
    unittest.main()
