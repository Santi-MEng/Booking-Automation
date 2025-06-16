import pytest
import json
from time import sleep
from pages.home_page import HomePage
from pages.search_results_page import Search_results

test_data_path='data/test_data.json'
with open(test_data_path) as f: #To open the Json file where it contains the data
    data=json.load(f) #To load the information from the file
    test_list = data["data"]



@pytest.mark.parametrize("test_list_item",test_list)
def test_booking(set_driver,test_list_item):
    driver=set_driver
    homepage=HomePage(driver)
    homepage.load()
    homepage.genius()
    homepage.accept_cookies()
    homepage.location(test_list_item["location"])
    homepage.select_dates(test_list_item["check-in"],test_list_item["check-out"])
    #homepage.guest()
    homepage.click_search()
    #New Page
    homepage.accept_cookies()
    homepage.genius()
    search_results=Search_results(driver)
    search_results.location_validation(test_list_item["location"])
    search_results.filter_hotel_selection()
    search_results.final_validations(test_list_item["check-in"],test_list_item["check-out"])
    sleep(5)
