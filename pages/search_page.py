from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MapsSearchPage:

    SEARCH_INPUT = (By.ID, 'searchbox-directions')
    START_LOCATION = (By.XPATH, '//*[@id=\"sb_ifc51\"]/input')
    DESTINATION_LOCATION = (By.XPATH, '//*[@id=\"sb_ifc52\"]/input')
    URL = 'https://www.google.com/maps'
    FIRST_RESULT = (By.CSS_SELECTOR, "[id^=section-directions-trip")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def click_directions(self):
        click_directions = self.browser.find_element(*self.SEARCH_INPUT)
        click_directions.click()

    def search_start_location(self, phrase):
        search_input = self.browser.find_element(*self.START_LOCATION)
        search_input.send_keys(phrase)

    def search_destination_location(self, phrase):
        search_input = self.browser.find_element(*self.DESTINATION_LOCATION)
        search_input.send_keys(phrase + Keys.RETURN)

    def search_results_are_displayed(self):
        first_search_result = self.browser.find_element(*self.FIRST_RESULT)
        return first_search_result.is_displayed()
