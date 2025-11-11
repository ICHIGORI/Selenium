import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.base_url = base_url
        self.time_expectation = 1.6

    def __driver_wait(self, time_expectation=None):
        return WebDriverWait(self.driver,
                             timeout=time_expectation if time_expectation else self.time_expectation,
                             poll_frequency=.2)

    def wait(self, timer: int | float = 3):
        time.sleep(timer)

    def get(self, url: str = None):
        self.driver.get(url) if url else self.driver.get(self.base_url)
        return self

    def assert_that(self, is_, that_, message="Assert failed", time_expectation=3):
        try:
            assert is_ == that_, f"[!]{message}"
        except TimeoutException:
            print(f"[!]{message} with time: {time_expectation}")

    def assert_enabled(self, element, message="Assert failed", time_expectation=None):
        wait = self.__driver_wait(time_expectation)
        wait.until(lambda _: element.is_enabled(), f"[!]{message}")

    def assert_displayed(self, element, message="Assert failed", time_expectation=None):
        wait = self.__driver_wait(time_expectation)
        wait.until(lambda _: element.is_displayed(), f"[!]{message}")

    def assert_not_displayed(self, element, message="Assert failed", time_expectation=None):
        try:
            self.wait(0.4)
            wait = self.__driver_wait(time_expectation)
            wait.until(lambda _: element.is_displayed(), f"[!]{message}")
            raise AssertionError(f"[!]{message}")
        except TimeoutException:
            return self

    def assert_not_enabled(self, element, message="Assert failed", time_expectation=None):
        try:
            wait = self.__driver_wait(time_expectation)
            wait.until(lambda _: element.is_enabled(), f"[!]{message}")
            raise AssertionError(f"[!]{message}")
        except TimeoutException:
            return self

    def find_element(self, locator: tuple[str, str], time_expectation=3):
        try:
            element = WebDriverWait(self.driver, time_expectation).until(
                EC.presence_of_element_located(locator),
                message=f"[!]Can't find element by locator {locator}"
            )
            return element
        except NoSuchElementException:
            print(f"[!]Element no found\n by locator{locator}")
        except TimeoutException:
            print(f"[!]Can't find element by locator {locator} with time: {time_expectation}")
            raise TimeoutException

    def find_elements(self, locator: tuple[str, str], time_expectation=3):
        try:
            elements = WebDriverWait(self.driver, time_expectation).until(
                EC.presence_of_all_elements_located(locator),
                message=f"[!]Can't find elements by locator {locator}"
            )
            return elements
        except NoSuchElementException:
            print(f"[!]Element no found\n by locator{locator}")
        except TimeoutException:
            print(f"[!]Can't find element by locator {locator} with time: {time_expectation}")
            raise TimeoutException

    def find_element_by_id(self, element_id: str):
        return self.find_element((By.ID, element_id))

    def find_element_by_class_name(self, element_id: str):
        return self.find_element((By.CLASS_NAME, element_id))

    def find_element_by_xpath(self, element_xpath: str):
        return self.find_element((By.XPATH, element_xpath))
