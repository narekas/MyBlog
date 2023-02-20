from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

class BasicInstallTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
         self.browser.quit()

    def test_home_page_title(self):  
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Blog', self.browser.title)  

    def test_home_page_header(self):
        self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Blog', header.text)


if __name__ == '__main__':  
    unittest.main()