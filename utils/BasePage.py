import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.base_url = base_url

    def wait(self, timer: int = 3):
        time.sleep(timer)

    def get(self, url: str = None):
        self.driver.get(url) if url else self.driver.get(self.base_url)
        return self

    def find_element(self, by: str, element: str):
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((by, element)),
                message=f"Can't find element by locator {(by, element)}"
            )
        except NoSuchElementException:
            print(f"[!]Element no found\n{element}")
        except Exception as e:
            print(f"[!]Some error: {e}")

        return element if element else None

    def find_element_by_id(self, element_id: str):
        return self.find_element(By.ID, element_id)

    def find_element_by_class_name(self, element_id: str):
        return self.find_element(By.CLASS_NAME, element_id)

    def find_element_by_xpath(self, element_xpath: str):
        return self.find_element(By.XPATH, element_xpath)
