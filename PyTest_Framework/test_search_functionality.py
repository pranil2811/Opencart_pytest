import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import object_repository as os
import common_functions as cf


@pytest.mark.usefixtures("setup")
def test_tc_sf_001(setup, data):
    # Access 'driver' via the 'login' fixture
    driver = setup
    url = data['URL']  # Get the URL from the data fixture
    driver.get(url)
    searchBox = driver.find_element(By.XPATH, os.search_bar)
    cf.send_keys_to_element(driver, searchBox, "iMac", 20)
    searchIcon = driver.find_element(By.XPATH, os.search_icon)
    cf.click_element(driver, searchIcon, 30)
    time.sleep(5)
    iMacProduct = driver.find_element(By.XPATH, os.product_imac)
    cf.assert_element_text(iMacProduct, "iMac")
    time.sleep(5)
