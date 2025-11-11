import pytest

from pages.google_page import GoogleLocators
from utils.Chrome import Chrome


class TestGoogle:
    def setup_class(self):
        self.browser = Chrome("https://www.google.com")
        self.driver = self.browser.driver
        self.actions = self.browser.actions
        self.input_text = "fff"

    def setup_method(self):
        self.browser.get()

    def teardown_class(self):
        self.driver.quit()

    def test_search_line_enabled(self):
        """Тест-кйст: Проверка доступности для взаимодействия поисковой строки
        -Открыть страницу google.com
        -Найти поисковую строку
        -Проверить что поисковая строка доступна для взаимодействия
        """
        search_line = self.browser.find_element(GoogleLocators.input_search_line)
        self.browser.assert_enabled(search_line)

    def test_search_line_displayed(self):
        """Тест-кйст: Проверка отображения поисковой строки
        -Открыть страницу google.com
        -Найти поисковую строку
        -Проверить что поисковая строка отображается
        """
        search_line = self.browser.find_element(GoogleLocators.input_search_line)
        self.browser.assert_displayed(search_line)

    @pytest.mark.parametrize("input_text", ["скумбрия", "котлеты"])
    def test_correct_search_result(self, input_text):
        """Тест-кйст: Проверка всплывающих подсказок
        -Открыть страницу google.com
        -Ввести в поисковую строку текст
        -Проверить в выпадающем меню подсказок, что подсказки содержат введёный текст
        """
        search_line = self.browser.find_element(GoogleLocators.input_search_line)
        self.actions.move_to_element(search_line).click().send_keys(input_text).perform()
        self.browser.wait(0.3)
        li_search_assist_list = self.browser.find_elements(GoogleLocators.li_search_assist_list)
        for search_assist in li_search_assist_list:
            assert input_text in search_assist.text.lower(), "текст подсказки не имеет искомого текста"
        self.browser.wait(1)

    @pytest.mark.parametrize("input_text, correct_text", [("фиизика","физика"),
                                                          ("фиика","физика"),
                                                          ("физикa","физика")])
    def test_correct_request_editing(self, input_text, correct_text):
        """Тест-кйст: Проверка всплывающих подсказок
        -Открыть страницу google.com
        -Ввести в поисковую строку текст с ошибкой
        -Проверить в выпадающем меню подсказок, что подсказки содержат введёный текст с исправленной ошибкой
        """
        search_line = self.browser.find_element(GoogleLocators.input_search_line)
        self.actions.move_to_element(search_line).click().send_keys(input_text).perform()
        self.browser.wait(0.3)
        li_search_assist_list = self.browser.find_elements(GoogleLocators.li_search_assist_list)
        for search_assist in li_search_assist_list:
            assert correct_text in search_assist.text.lower(), "текст подсказки не имеет исправленного текста текста"
        self.browser.wait(1)

    def test_search_arrow_clear(self):
        """Тест-кйст: Проверка отображения кнопки отчистки поисковой строки
        -Открыть страницу google.com
        -Кнопка отчистки поисковой строки не отображается
        -Ввести в поисковую строку текст
        -Кнопка отчистки поисковой строки отображается
        """
        search_line = self.browser.find_element(GoogleLocators.input_search_line)
        btn_arrow_clear = self.browser.find_element(GoogleLocators.btn_arrow_clear)
        self.browser.assert_not_displayed(btn_arrow_clear)
        self.actions.move_to_element(search_line).click().send_keys(self.input_text).perform()
        self.browser.assert_displayed(btn_arrow_clear)

    def test_clear_arrow_clear(self):
        """Тест-кйст: Проверка отчистки поискового запроса, кнопкой отчистки поисковой строки
        -Открыть страницу google.com
        -Ввести в поисковую строку текст
        -Проверить значение поисковой строки, на соответствие введенному тексту
        -Нажать кнопку отчистки поисковой строки
        -Проверить значение поисковой строки, значение пустое
        """
        search_line = self.browser.find_element(GoogleLocators.input_search_line)
        btn_arrow_clear = self.browser.find_element(GoogleLocators.btn_arrow_clear)

        self.actions.move_to_element(search_line).click().send_keys(self.input_text).perform()
        assert self.input_text == search_line.get_attribute("value"), \
            "Текст поисковой строки не совпадает с введенным текстом"
        btn_arrow_clear.click()
        assert search_line.get_attribute("value") == '', "Текст поисковой строки не отчистился"

    def test_open_arrow_common_keyboard(self):
        """Тест-кйст: Проверка открытия виртуальной клавиатуры
        -Открыть страницу google.com
        -Кнопка виртуальной клавиатуры отображается
        -Нажать кнопку виртуальной клавиатуры
        -Отобразился блок виртуальной клавиатуры
        """
        btn_virtual_keyboard = self.browser.find_element(GoogleLocators.btn_virtual_keyboard)
        self.browser.assert_displayed(btn_virtual_keyboard)
        self.actions.move_to_element(btn_virtual_keyboard).click().perform()
        virtual_keyboard = self.browser.find_element(GoogleLocators.div_virtual_keyboard)
        self.browser.assert_displayed(virtual_keyboard)
