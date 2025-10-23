import pytest

from pages.dzen_page import DzenLocators
from utils.Chrome import Chrome


class TestDzen:

    def setup_class(self):
        self.chrome = Chrome("https://dzen.ru/")
        self.driver = self.chrome.driver

    def setup_method(self):
        self.chrome.get()
        self.chrome.wait(1)

    def teardown_class(self):
        self.chrome.driver.quit()

    def test_search_arrow_clear(self):
        """Тест-кйст: Проверка отображения кнопки отчистки поисковой строки
        -Открыть страницу dzen.ru
        -Кнопки отчистки поисковой строки не отображается
        -Ввести в поисковую строку текст
        -Кнопки отчистки поисковой строки отображается
        """

        frame_iframe = self.driver.find_element(*DzenLocators.frame_iframe)
        self.driver.switch_to.frame(frame_iframe)
        btn_arrow_clear = self.driver.find_element(*DzenLocators.btn_arrow_clear)
        assert btn_arrow_clear.is_enabled() is True
        element = self.driver.find_element(*DzenLocators.input_search_line)
        element.click()
        element.send_keys("fff")
        self.chrome.wait(1)
        assert btn_arrow_clear.is_displayed() is True

    def test_search_arrow_common_keyboard(self):
        """Тест-кйст: Проверка отображения кнопки виртуальной клавиатуры
        -Открыть страницу dzen.ru
        -Кнопки виртуальной клавиатуры отображается
        -Ввести в поисковую строку текст
        -Кнопка виртуальной клавиатуры не отображается
        """

        frame_iframe = self.driver.find_element(*DzenLocators.frame_iframe)
        keyboard = self.driver.find_element(*DzenLocators.btn_a_virtual_keyboard)
        assert keyboard.is_displayed() is True
        self.driver.switch_to.frame(frame_iframe)
        element = self.driver.find_element(*DzenLocators.input_search_line)
        element.click()
        element.send_keys("fff")
        self.chrome.wait(1)
        self.driver.switch_to.default_content()
        assert keyboard.is_enabled() is True

