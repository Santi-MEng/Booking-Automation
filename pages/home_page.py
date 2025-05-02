
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class HomePage:
    def __init__(self,driver):
        self.driver= driver
        self.wait=WebDriverWait(self.driver,10)
        self.url="https://www.booking.com"

    def load(self):
        self.driver.get(self.url)

    def accept_cookies(self):
        #Accept cookies
        try:
            accept_btn = self.wait.until(expected_conditions.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
            accept_btn.click()
        except:
            pass
        try:
            #Genius option
            close_btn=self.driver.find_element(By.XPATH,"//button[@aria-label='Dismiss sign-in info.']")
            close_btn.click()
        except:
            pass

    def location(self,place):
        search_bar=self.driver.find_element(By.XPATH,"//input[@name='ss']")
        search_bar.send_keys(place)
        sleep(2)
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='a3332d346a d2f04c9037']"))).click()



    def select_dates(self,checkIn,checkOut):
        while True:
            try:
                self.driver.find_element(By.CSS_SELECTOR, f"span[data-date='{checkIn}']").click()
                break
            except NoSuchElementException:
                # Click next month button
                next_button = self.driver.find_element(By.XPATH,"//button[@class='a83ed08757 c21c56c305 f38b6daa18 d691166b09 f671049264 f4552b6561 dc72a8413c f073249358']")
                next_button.click()
                sleep(0.5)  # Slight wait for loading
        while True:
            try:
                self.driver.find_element(By.CSS_SELECTOR, f"span[data-date='{checkOut}']").click()
                break
            except NoSuchElementException:
                # Click next month button
                next_button = self.driver.find_element(By.XPATH,"//button[@class='a83ed08757 c21c56c305 f38b6daa18 d691166b09 f671049264 f4552b6561 dc72a8413c f073249358']")
                next_button.click()
                sleep(0.5)  # Slight wait for loading
    def guest(self):
        self.driver.find_element(By.XPATH,"//div/div[@class='d777d2b248']").click()
        if self.driver.find_element(By.ID, "group_adults").get_attribute("value")=="2":
            pass
        self.driver.find_element(By.XPATH,"//span[contains(.,'Done')]").click()

    def click_search(self):
        self.driver.find_element(By.XPATH,"//div[@class='e22b782521 d12ff5f5bf']").click()








