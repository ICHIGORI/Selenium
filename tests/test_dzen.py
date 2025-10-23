import pytest
from tests.pages.dzen_page import DzenLocators
from utils.Chrome import Chrome


@pytest.mark.search
def test_search_arrow_clear():
    """Тест-кйст: Проверка отображения кнопки отчистки поисковой строки
    -Открыть страницу dzen.ru
    -Кнопки отчистки поисковой строки не отображается
    -Ввести в поисковую строку текст
    -Кнопки отчистки поисковой строки отображается
    """
    chrome = Chrome("https://dzen.ru/")
    chrome.get()
    driver = chrome.driver
    chrome.wait(2)

    frame_iframe = driver.find_element(*DzenLocators.frame_iframe)
    driver.switch_to.frame(frame_iframe)
    btn_arrow_clear = driver.find_element(*DzenLocators.btn_arrow_clear)
    assert btn_arrow_clear.is_enabled() is True
    element = driver.find_element(*DzenLocators.input_search_line)
    element.click()
    element.send_keys("fff")
    chrome.wait(1)
    assert btn_arrow_clear.is_displayed() is True

    chrome.driver.quit()


def test_search_arrow_common_keyboard():
    """Тест-кйст: Проверка отображения кнопки виртуальной клавиатуры
    -Открыть страницу dzen.ru
    -Кнопки виртуальной клавиатуры отображается
    -Ввести в поисковую строку текст
    -Кнопка виртуальной клавиатуры не отображается
    """
    chrome = Chrome("https://dzen.ru/")
    chrome.get()
    driver = chrome.driver
    chrome.wait(2)

    frame_iframe = driver.find_element(*DzenLocators.frame_iframe)
    keyboard = driver.find_element(*DzenLocators.btn_a_virtual_keyboard)
    assert keyboard.is_displayed() is True
    driver.switch_to.frame(frame_iframe)
    element = driver.find_element(*DzenLocators.input_search_line)
    element.click()
    element.send_keys("fff")
    chrome.wait(1)
    driver.switch_to.default_content()
    assert keyboard.is_enabled() is True

    chrome.driver.quit()
