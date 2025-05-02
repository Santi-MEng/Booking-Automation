from selenium import webdriver



def init_browser():
    driver=webdriver.Edge()
    driver.implicitly_wait(5)
    return driver