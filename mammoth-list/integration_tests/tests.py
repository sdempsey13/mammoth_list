from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class LinksApp(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_can_visit_root_page(self):
        self.selenium.get(self.live_server_url)

        self.assertIn('Django', self.selenium.title)
