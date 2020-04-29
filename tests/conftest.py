import pytest
import selenium.webdriver


@pytest.fixture()
def browser():

    b = selenium.webdriver.Chrome("/Users/ianbush/Documents/drivers/chromedriver")
    b.implicitly_wait(20)

    yield b

    b.quit()
