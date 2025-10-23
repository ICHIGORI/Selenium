from utils.Chrome import Chrome
from pages.dzen_page import DzenLocators
from pages.yandex_page import YandexLocators


def dzen_search_arrow_clear():
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


def dzen_search_arrow_common_keyboard():
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


def yandex_images():
    chrome = Chrome("https://yandex.ru/all")
    chrome.get()

    element = chrome.find_element(*YandexLocators.btn_service_images)
    element.click()
    chrome.driver.switch_to.window(chrome.driver.window_handles[1])
    element = chrome.find_element(*YandexLocators.div_first_images_post)
    element.click()

    chrome.driver.quit()


if __name__ == "__main__":
    dzen_search_arrow_clear()
    dzen_search_arrow_common_keyboard()
    yandex_images()
