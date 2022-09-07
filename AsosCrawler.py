from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time, requests


class AsosCrawler:
    def __init__(self, url, binary_location, driver_location):
        self.url = url
        self.binary_location = binary_location
        self.driver_location = driver_location
        self.driver = None
        self.token = "5685048113:AAGiS9VST00_lsab_wZazEqChaFpNVL63hc"
        self.chat_id = "1131501097"

    def get_driver(self):
        options = webdriver.ChromeOptions()
        options.binary_location = self.binary_location

        driver = webdriver.Chrome(executable_path=self.driver_location, chrome_options=options)

        self.driver = driver

    def get_page(self):
        self.get_driver()
        self.driver.get(self.url)

    def quit_driver(self):
        self.driver.quit()

    def send_message(self, text):
        url_req = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={text}"
        result = requests.get(url=url_req)
        print(result.json())

    def parse_size(self, text, size_list):
        text_list = list(text.split(" "))
        for part in size_list:
            if part not in text_list:
                return False
        return True

    def check_size(self, size):
        self.get_page()
        select = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "main-size-select-0")))
        if select:
            options = select.find_elements(By.TAG_NAME, "option")
            for option in options:
                if self.parse_size(option.text, list(size.split(" "))):
                    if "Out of stock" in option.text:
                        self.send_message(f"Size {size} is unavailable :(")
                    else:
                        self.send_message(f"Size {size} is available!\n{self.url}")
        else:
            self.send_message("Didn't find sizes element, check your code!")

        time.sleep(3)
        self.quit_driver()
