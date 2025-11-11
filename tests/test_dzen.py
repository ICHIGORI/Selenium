import pytest
from pages.dzen_page import DzenLocators


@pytest.mark.usefixtures("browser_instance")
class TestDzen:

    def setup_method(self):
        self.driver = self.browser.driver
        self.actions = self.browser.actions
        self.input_text = "fff"
        self.browser.get()

    def test_search_line_enabled(self):
        """Тест-кйст: Проверка доступности для взаимодействия поисковой строки
        -Открыть страницу dzen.ru
        -Найти поисковую строку
        -Проверить что поисковая строка доступна для взаимодействия
        """
        frame_iframe = self.browser.find_element(DzenLocators.frame_iframe)
        self.driver.switch_to.frame(frame_iframe)
        input_line = self.browser.find_element(DzenLocators.input_search_line)
        self.browser.assert_enabled(input_line, "Поисковая строка не доступна для взаимодействия")

    def test_search_line_displayed(self):
        """Тест-кйст: Проверка отображения поисковой строки
        -Открыть страницу dzen.ru
        -Найти поисковую строку
        -Проверить что поисковая строка отображается
        """
        frame_iframe = self.browser.find_element(DzenLocators.frame_iframe)
        self.driver.switch_to.frame(frame_iframe)
        input_line = self.browser.find_element(DzenLocators.input_search_line)
        self.browser.assert_displayed(input_line, "Поисковая строка не отображается")

    @pytest.mark.parametrize("input_text", ["скумбрия", "котлеты"])
    def test_correct_search_result(self, input_text):
        """Тест-кйст: Проверка всплывающих подсказок
        -Открыть страницу dzen.ru
        -Ввести в поисковую строку текст
        -Проверить в выпадающем меню подсказок, что подсказки содержат введёный текст
        """
        frame_iframe = self.browser.find_element(DzenLocators.frame_iframe)
        self.driver.switch_to.frame(frame_iframe)
        input_line = self.browser.find_element(DzenLocators.input_search_line)
        self.actions.move_to_element(input_line).click().send_keys(input_text).perform()
        assist_list = self.browser.find_elements(DzenLocators.li_search_assist_list)
        for element in assist_list:
            assert input_text in element.text.lower(), "текст подсказки не имеет искомого текста"

    @pytest.mark.parametrize("input_text, correct_text", [("скубрия","скумбрия"),
                                                            ("скуvбрия","скумбрия"),
                                                            ("cкумбрия","скумбрия")])
    def test_correct_request_editing(self, input_text, correct_text):
        """Тест-кйст: Проверка всплывающих подсказок
        -Открыть страницу dzen.ru
        -Ввести в поисковую строку текст с ошибкой
        -Проверить в выпадающем меню подсказок, что подсказки содержат введёный текст с исправленной ошибкой
        """
        frame_iframe = self.browser.find_element(DzenLocators.frame_iframe)
        self.driver.switch_to.frame(frame_iframe)
        input_line = self.browser.find_element(DzenLocators.input_search_line)
        self.actions.move_to_element(input_line).click().send_keys(input_text).perform()
        assist_list = self.browser.find_elements(DzenLocators.li_search_assist_list)
        for element in assist_list:
            assert input_text not in element.text.lower(), "текст подсказка имеет не исправленный искомый текст"
            assert correct_text in element.text.lower(), "текст подсказки не имеет искомого, исправленного текста"

    def test_search_arrow_clear(self):
        """Тест-кйст: Проверка отображения кнопки отчистки поисковой строки
        -Открыть страницу dzen.ru
        -Кнопка отчистки поисковой строки не отображается
        -Ввести в поисковую строку текст
        -Кнопка отчистки поисковой строки отображается
        """

        keyboard = self.browser.find_element(DzenLocators.btn_a_virtual_keyboard)
        self.browser.assert_displayed(keyboard, "Кнопка виртуальной клавиатуры не отображается")
        frame_iframe = self.browser.find_element(DzenLocators.frame_iframe)
        self.driver.switch_to.frame(frame_iframe)
        btn_arrow_clear = self.browser.find_element(DzenLocators.btn_arrow_clear)
        self.browser.assert_not_displayed(btn_arrow_clear, "Кнопка отчистки отображается, но не должна")
        element = self.browser.find_element(DzenLocators.input_search_line)
        element.send_keys(self.input_text)
        self.browser.assert_displayed(btn_arrow_clear, "Кнопка отчистки не отображается")

    def test_search_arrow_common_keyboard(self):
        """Тест-кйст: Проверка отображения кнопки виртуальной клавиатуры
        -Открыть страницу dzen.ru
        -Кнопка виртуальной клавиатуры отображается
        -Ввести в поисковую строку текст
        -Кнопка виртуальной клавиатуры не отображается
        """

        frame_iframe = self.browser.find_element(DzenLocators.frame_iframe)
        keyboard = self.browser.find_element(DzenLocators.btn_a_virtual_keyboard)
        self.browser.assert_displayed(keyboard, "Кнопка виртуальной клавиатуры не отображается")
        self.driver.switch_to.frame(frame_iframe)
        element = self.browser.find_element(DzenLocators.input_search_line)
        element.send_keys(self.input_text)
        self.driver.switch_to.default_content()
        self.browser.wait(0.6)
        self.browser.assert_not_displayed(keyboard, "Кнопка виртуальной клавиатуры не перестала отображаться")

    def test_clear_arrow_clear(self):
        """Тест-кйст: Проверка отчистки поискового запроса, кнопкой отчистки поисковой строки
        -Открыть страницу dzen.ru
        -Ввести в поисковую строку текст
        -Проверить значение поисковой строки, на соответствие введенному тексту
        -Нажать кнопку отчистки поисковой строки
        -Проверить значение поисковой строки, значение пустое
        """

        frame_iframe = self.browser.find_element(DzenLocators.frame_iframe)
        self.browser.wait(1)
        self.driver.switch_to.frame(frame_iframe)
        element = self.browser.find_element(DzenLocators.input_search_line)
        element.send_keys(self.input_text)
        assert self.input_text == element.get_attribute('value'), \
            f"Значение поисковой строки не равно строке: {self.input_text}"
        btn_arrow_clear = self.browser.find_element(DzenLocators.btn_arrow_clear)
        btn_arrow_clear.click()
        assert "" == element.get_attribute('value'), \
            f"Значение поисковой строки не отчищено и содержит значение: {element.get_attribute('value')}"

    def test_open_arrow_common_keyboard(self):
        """Тест-кйст: Проверка открытия виртуальной клавиатуры
        -Открыть страницу dzen.ru
        -Кнопка виртуальной клавиатуры отображается
        -Нажать кнопку виртуальной клавиатуры
        -Отобразился блок виртуальной клавиатуры
        """

        keyboard = self.browser.find_element(DzenLocators.btn_a_virtual_keyboard)
        self.browser.assert_displayed(keyboard, "Кнопка открытия виртуальной клавиатуры не отображается")
        keyboard.click()
        virtual_keyboard = self.browser.find_element(DzenLocators.div_virtual_keyboard)
        self.browser.assert_displayed(virtual_keyboard, "Виртуальная клавиатура не отображается")
