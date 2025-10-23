from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from utils.BasePage import BasePage
from base_path import CHROMEDRIVER_PATH
from utils.config_parser import get_config_list


class Chrome(BasePage):

    def __init__(self, base_url):

        self.chrome_options = Options()
        self.config = get_config_list()
        for arg in self.config:
            self.chrome_options.add_argument(arg)
        super().__init__(webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=self.chrome_options), base_url)
