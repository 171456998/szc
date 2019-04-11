import time
def send_key(driver,xpath):
    username = driver.find_element_by_xpath(xpath)
    username.click()

    time.sleep(1)
    pass