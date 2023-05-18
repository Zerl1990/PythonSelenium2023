from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = " https://demoqa.com/select-menu"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get(URL)

    def test_old_style_select(self):
        element = self.driver.find_element(By.ID, "oldSelectMenu")
        select = Select(element)
        select.select_by_value()

    def teardown_method(self):
        self.driver.quit()
