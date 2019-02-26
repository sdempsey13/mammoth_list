from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_visit_root_page(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('Django', self.browser.title)
