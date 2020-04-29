from pages import search_page
from pages.search_page import MapsSearchPage


def test_search_results_are_displayed(browser):
    search_page = MapsSearchPage(browser)
    START_LOCATION = "Orlando, FL"
    END_LOCATION = "San Francisco, CA"

    # Given I navigate to the search page
    search_page.load()

    # When I enter my start location
    search_page.click_directions()
    search_page.search_start_location(START_LOCATION)

    # And I enter my destination
    search_page.search_destination_location(END_LOCATION)

    # Then results are displayed
    assert search_page.search_results_are_displayed()
