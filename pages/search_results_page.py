from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.calendar import calendar_check
from utils.reports import save_report


class Search_results:
    def __init__(self,driver,):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 15)
        self.hotel_info={}

    def location_validation(self,place_name):
        place=self.driver.find_element(By.XPATH,"//h1[@class='b87c397a13 cacb5ff522']").text
        assert place_name in place

    def filter_hotel_selection(self):
        hotel_box=self.driver.find_element(By.XPATH,"//div[text()='Hotels']")
        hotel_box.click()

        try:
            # Wait until at least one hotel appears
            hotels = self.wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-testid="property-card"]')))
            # Click the first hotel
            hotels[0].find_element(By.CSS_SELECTOR,"a div[data-testid='title']").click()
            print("First hotel clicked!")
            tabs = self.driver.window_handles  # this line gets a list with the possible opened tabs
            self.driver._switch_to.window(tabs[-1]) #this line gets to the most recent tab
        except Exception as e: #e stands for no element found
            print(f"No hotels found or error occurred: {e}")

    def final_validations(self,check_in,check_out):
        hotel_name=self.driver.find_element(By.XPATH,"//h2[@class='ddb12f4f86 pp-header__title']").text
        self.hotel_info['hotel_name']=hotel_name
        address=self.driver.find_element(By.XPATH,"//div[@class='b99b6ef58f cb4b7a25d9']").text
        self.hotel_info["address_info"]=address
        prices=self.driver.find_elements(By.XPATH,"//span[@class='prco-valign-middle-helper']")
        self.hotel_info["price"]=prices[0].text
        score=self.driver.find_element(By.XPATH,"//div[@data-testid='review-score-right-component']/div/div[@class='ac4a7896c7']").text
        self.hotel_info["score"]=score
        print(self.hotel_info)
        check_in_date=self.driver.find_element(By.XPATH,"//button[contains(@data-testid,'date-display-field-start')]/span").text
        check_out_date=self.driver.find_element(By.XPATH,"//button[contains(@data-testid,'date-display-field-end')]/span").text
        chin,chout=calendar_check(check_in_date,check_out_date)
        assert chin in check_in
        print(f"check_in to validate: {check_in}, check_in received: {chin}")
        assert chout in check_out
        print(f"check_out to validate: {check_out}, check_out received: {chout}")
        print(self.hotel_info)
        save_report(self.hotel_info)