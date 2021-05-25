from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from settings import *


class AdminPanel:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    DRIVER = webdriver.Chrome(SELENIUM_CUSTOM_CHROME_PATH, options=options)
    DRIVER.get(URL_LOGIN)

    def __init__(self, login, password):
        self.DRIVER.find_element_by_xpath('//*[@id="id_username"]').send_keys(login)
        self.DRIVER.find_element_by_xpath('//*[@id="id_password"]').send_keys(password)
        self.DRIVER.find_element_by_xpath('/html/body/div/div/div/div[2]/form/div/div/button').submit()

    def go_to_products(self):
        self.DRIVER.get(URL_PRODUCTS)

    def add_new_product(self, data):
        print(data)
        self.go_to_products()
        self.DRIVER.find_element_by_xpath('/html/body/div[1]/div/div/a').click()
        time.sleep(2)
        self.DRIVER.find_element_by_xpath(f'//input[@value="{data["type"]}"]').click()
        self.DRIVER.find_element_by_xpath('//*[@id="base-modal"]/form/div[2]/button').click()
        time.sleep(2)
        self.DRIVER.find_element_by_xpath('//*[@id="id_name"]').send_keys(data['title'])
        # self.DRIVER.find_element_by_xpath('//*[@id="id_description"]').click()
        self.DRIVER.find_element_by_xpath('//*[@id="id_price_0"]').send_keys(data['price'])
        self.DRIVER.find_element_by_xpath('//*[@id="form-product"]/div[1]/div/div[2]/div[2]/div/div/input').click()
        time.sleep(1)
        element = self.DRIVER.find_element_by_xpath('//*[@id="form-product"]/div[1]/div/div[2]/div[2]/div/div/ul')
        print(element.text)
        element = element.find_element_by_xpath(f'.//li[{element.text.split(chr(10)).index(data["company"])+1}]')
        # print(element.get_attribute('innerHTML'))
        action = ActionChains(self.DRIVER)
        action.click(on_element=element).perform()

        # /html/body/main/div[3]/div[1]/div/div[1]/form/div[1]/div/div[2]/div[5]/div/div/ul
        self.DRIVER.find_element_by_xpath('//*[@id="select2-id_attribute-khorovac-1-container"]').click()
        time.sleep(1)

        element = self.DRIVER.find_element_by_xpath('/html/body/main/div[3]/div[1]/div/div[1]/form/div[1]/div/div[2]/div[5]/div/div/ul')
        print(element.text)
        print(element.get_attribute('innerHTML'))
        # action.click(on_element=element).perform()
        # self.DRIVER.find_element_by_xpath(f'//li/span[contains(text(), Թումանյանս)]').click()
        # self.DRIVER.find_element_by_xpath('//*[@id="id_name"]').send_keys(data['title'])


        time.sleep(10)

    def add_new_products(self, products):
        for data in products:
            self.add_new_product(data)

    def close(self):
        time.sleep(4)
        self.DRIVER.close()

    def multiselect_set_selections(driver, element, labels):
        # el = driver.find_element_by_id(element_id)
        for option in element.find_elements_by_tag_name('option'):
            if option.text in labels:
                option.click()


if __name__ == '__main__':

    admin_panel = AdminPanel(login=LOGIN, password=PASSWORD)


    from data import products_data

    admin_panel.add_new_products(products_data)

    admin_panel.close()