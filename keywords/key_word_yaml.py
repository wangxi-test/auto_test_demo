

# PO模式的关键词
import time
from selenium import webdriver


class BasePage:
    # driver = webdriver.Chrome()
    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def locator(self,**kwargs):
        return self.driver.find_element(kwargs['name'],kwargs['value'])

    def input(self,**kwargs):
        self.locator(**kwargs).send_keys(kwargs['txt'])

    def click(self,**kwargs):
        self.locator(**kwargs).click()

    def wait(self,time_):
        time.sleep(time_)

    def save_screen(self,path):
        self.driver.save_screenshot(path)
