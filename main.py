import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def run_bot():
    driver = webdriver.Firefox()
    driver.get("https://visa.vfsglobal.com/blr/en/pol/login")
    wait = WebDriverWait(driver, 6)  # seconds
    try:
        # Find button to accept cookies
        cookie_button = wait.until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
    except TimeoutException:
        print("Loading took too much time!")
    ActionChains(driver).click(cookie_button).perform()

    # Find input field to enter login
    login = driver.find_element_by_id('mat-input-0')
    login.send_keys("attiverr@yandex.ru")

    # Find pass field to enter pass
    pswd = driver.find_element_by_id('mat-input-1')
    pswd.send_keys("22GSM10i$")

    # Find button to sign in
    sign_button = driver.find_element_by_class_name('mat-button-base')
    time.sleep(1)
    ActionChains(driver).move_to_element(sign_button).click().perform()

    try:
        start_new_booking = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'd-lg-inline-block')))
        # start_new_booking = driver.find_element_by_class_name('d-lg-inline-block')
    except TimeoutException:
        print("Loading took too much time!")
    ActionChains(driver).move_to_element(start_new_booking).click().perform()



    # driver.save_screenshot() # save screenshot
    # driver.close()


if __name__ == '__main__':
    run_bot()
