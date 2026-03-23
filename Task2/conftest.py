import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(1)
    driver.get("https://cerulean-praline-8e5aa6.netlify.app/")
    yield driver
    driver.quit()


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(params=[
    {"deviceName": "iPhone 12 Pro"},
    {"deviceName": "iPhone SE"},
    {"deviceName": "Pixel 7"},
    {"deviceName": "Samsung Galaxy S20 Ultra"},
    {"width": 375, "height": 667, "pixelRatio": 2.0}
])
def mobile_driver(request):
    options = Options()

    if "deviceName" in request.param:
        options.add_experimental_option("mobileEmulation", request.param)
    else:
        mobile_emulation = {
            "deviceMetrics": {
                "width": request.param["width"],
                "height": request.param["height"],
                "pixelRatio": request.param["pixelRatio"]
            },
            "userAgent": "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36"
        }
        options.add_experimental_option("mobileEmulation", mobile_emulation)

    mobile_driver = webdriver.Chrome(options=options)
    mobile_driver.maximize_window()
    mobile_driver.implicitly_wait(10)
    mobile_driver.get("https://cerulean-praline-8e5aa6.netlify.app/")
    yield mobile_driver
    mobile_driver.quit()