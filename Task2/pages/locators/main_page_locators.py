from selenium.webdriver.common.by import By
class MainPageLocators:

    PRIORITY_TOGGLE = (By.XPATH,'//span[@class = "_urgentToggle__slider_h1vv9_21"]')
    CATEGORY_DROPDOWN = (By.XPATH,'//option[text()="Все категории"]/parent::select')
    PRICE_RANGE_FROM = (By.XPATH,'//input[@placeholder="От"]')
    PRICE_RANGE_UP_TO  = (By.XPATH,'//input[@placeholder="До"]')
    MODERATION_STATUS = (By.XPATH,'//label//span[text()="На модерации"]')
    APPROVED_STATUS = (By.XPATH,'//label//span[text()="Одобрено"]')
    DENIED_STATUS = (By.XPATH,'//label//span[text()="Отклонено"]')
    DRAFT_STATUS = (By.XPATH,'//label//span[text()="Черновик"]')
    PRIORITY_BADGE = (By.XPATH,'.//span[@class = "_card__priority_15fhn_172"]')
    SORTING_TYPE_DROPDOWN = (By.XPATH,'//option[text()="Цене"]/parent::select')
    SORTING_ORDER_DROPDOWN = (By.XPATH, '//option[text()="По убыванию"]/parent::select')
    ANNOUNCEMENT_TITLE = [(By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[1]/div[3]/div[1]/h3'),
                          (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[2]/div[3]/div[1]/h3'),
                          (By.XPATH, '//*[@id="root"]/div/div[2]/main/div[1]/div[3]/div[3]/div[1]/h3'),
                          (By.XPATH, '//*[@id="root"]/div/div[2]/main/div[1]/div[4]/div[3]/div[1]/h3'),
                          (By.XPATH, '//*[@id="root"]/div/div[2]/main/div[1]/div[5]/div[3]/div[1]/h3'),
                          (By.XPATH, '//*[@id="root"]/div/div[2]/main/div[1]/div[6]/div[3]/div[1]/h3'),
                          (By.XPATH, '//*[@id="root"]/div/div[2]/main/div[1]/div[7]/div[3]/div[1]/h3'),
                          (By.XPATH, '//*[@id="root"]/div/div[2]/main/div[1]/div[8]/div[3]/div[1]/h3'),
                          (By.XPATH, '//*[@id="root"]/div/div[2]/main/div[1]/div[9]/div[3]/div[1]/h3'),
                          (By.XPATH, '//*[@id="root"]/div/div[2]/main/div[1]/div[10]/div[3]/div[1]/h3'),
                          ]
    ANNOUNCEMENT_PRICE = [(By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[1]/div[3]/div[2]/div[1]'),
                          (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[2]/div[3]/div[2]/div[1]'),
                          (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[3]/div[3]/div[2]/div[1]'),
                          (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[4]/div[3]/div[2]/div[1]'),
                          (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[5]/div[3]/div[2]/div[1]'),
                          (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[6]/div[3]/div[2]/div[1]'),
                          (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[7]/div[3]/div[2]/div[1]'),
                          (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[8]/div[3]/div[2]/div[1]'),
                          (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[9]/div[3]/div[2]/div[1]'),
                          (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[10]/div[3]/div[2]/div[1]'),
                          ]
    NEXT_PAGE_BUTTON = (By.XPATH,'//button[@aria-label="Следующая страница"]')
    FIRST_PAGE_BUTTON = (By.XPATH,'//button[@aria-label="Первая страница"]')
    ANNOUNCEMENT_CARD = [(By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[1]'),
                         (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[2]'),
                         (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[3]'),
                         (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[4]'),
                         (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[5]'),
                         (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[6]'),
                         (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[7]'),
                         (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[8]'),
                         (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[9]'),
                         (By.XPATH,'//*[@id="root"]/div/div[2]/main/div[1]/div[10]'),]

    EMPTY_DASHBOARD_MESSAGE = (By.XPATH,'//div[@class="_empty_imlvm_312"]')



    @staticmethod
    def dropdown_value_locator(value):
        locator = (By.XPATH, f'//option[@value="{value}"]')
        return locator




