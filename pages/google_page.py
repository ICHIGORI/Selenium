from selenium.webdriver.common.by import By


class GoogleLocators:
    input_search_line = (By.NAME, 'q')
    ul_search_assist_list = (By.XPATH, "//ul[@class='G43f7e']")
    li_search_assist_list = (By.XPATH, "//ul[@class='G43f7e']/li")
    btn_arrow_clear = (By.CSS_SELECTOR, "div[aria-label='Очистить']")
    btn_virtual_keyboard = (By.CSS_SELECTOR, "div[aria-label='Экранная клавиатура']")
    div_virtual_keyboard = (By.ID, "kbd")
