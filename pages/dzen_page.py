from selenium.webdriver.common.by import By


class DzenLocators:
    frame_iframe = (By.XPATH, "//iframe[@class='dzen-search-arrow-common__frame']")
    input_search_line = (By.XPATH, "//input[@name='text']")
    btn_a_virtual_keyboard = (By.XPATH, "//a[@class='dzen-search-arrow-common__keyboard']")
    btn_arrow_clear = (By.CLASS_NAME, "arrow__clear")
    div_virtual_keyboard = (By.CLASS_NAME, "keyboard__popup")
    li_search_assist_list = (By.CLASS_NAME, "mini-suggest__item")

