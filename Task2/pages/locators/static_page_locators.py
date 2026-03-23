from selenium.webdriver.common.by import By

class StaticPageLocator:
    STATIC_PAGE = (By.XPATH,'//*[@id="root"]/nav/div/ul/li[2]')
    REFRESH_BUTTON = (By.XPATH,'//button[@class = "_refreshButton_ir5wu_16"]')
    STOP_TIMER_BUTTON = (By.XPATH,'//button[@class = "_toggleButton_ir5wu_69 _toggleButton_active_ir5wu_89"]')
    ACTIVATE_TIMER_BUTTON = (By.XPATH,'//button[@class="_toggleButton_ir5wu_69 "]')
    TIMER = (By.XPATH, '//span[@class = "_timeValue_ir5wu_112"]')
    DISABLED_TIMER_MESSAGE = (By.XPATH,'//div[@class = "_disabled_ir5wu_136"]//span')