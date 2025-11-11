from selenium import webdriver
from utils.BasePage import BasePage


class Firefox(BasePage):

    def __init__(self, base_url):

        self.firefox_options = webdriver.FirefoxOptions()
        super().__init__(webdriver.Firefox(options=self.firefox_options), base_url)
