from selenium import webdriver
from utils.BasePage import BasePage


class Edge(BasePage):

    def __init__(self, base_url):

        self.ie_options = webdriver.EdgeOptions()
        super().__init__(webdriver.Edge(options=self.ie_options), base_url)
