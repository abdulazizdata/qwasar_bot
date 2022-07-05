from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


def bot():

    url = "https://upskill.us.qwasar.io/"
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.find_element_by_xpath('//input[@id="username"]').send_keys(
        'abdulaziz.astrum@gmail.com')  # abdurahimovabubakr777@gmail.com
    driver.find_element_by_xpath('//input[@id="password"]').send_keys('zzxxcc99')  # AbuBakr0000
    driver.find_element_by_xpath(
        '//button[@class="btn bg-c-dark-blue text-c-white hover-text-c-dark-blue hover-bg-c-white border-black '
        'radius-1 w-100 m-b-10"]').click()
    while True:
        driver.find_element_by_xpath(
            '//a[@class="btn bg-c-dark-blue text-c-white hover-text-c-dark-blue hover-bg-c-white border-black '
            'radius-1 p-r-8 b-radius-3"]').click()
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())

            alert = driver.switch_to.alert
            alert.accept()
            # print("alert Exists in page")
        except TimeoutException:
            print("alert does not Exist in page")
        # sleep(8)
        # alert = Alert(driver)
        # alert.accept()
    driver.quit()
    driver.close()
    # alert = Alert(driver)
    # alert.accept()
    while True:
        pass



while True:
        try:
            bot()
        except:
            continue
        break


