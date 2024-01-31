from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

"""
Created on Fri Sep 29 23:59:57 2023

@author: pranil
"""

from selenium.webdriver.common.by import By
import object_repository as os
import pytest
import time
import common_functions as cf


@pytest.mark.usefixtures("setup")
def test_edit_my_account_info(login):
    driver = login
    edit_info = driver.find_element(By.XPATH, "//a[contains(text(),'Edit your account information')]")
    cf.click_element(driver, edit_info, 10)
    assert driver.title == "My Account Information"
    print("title", driver.title)
    time.sleep(5)
    first_name = driver.find_element(By.XPATH, os.edit_info_first_name)
    cf.send_keys_to_element(driver, first_name, "Mahesh", 10)
    last_name = driver.find_element(By.XPATH, os.edit_info_last_name)
    cf.send_keys_to_element(driver, last_name, "Narad", 10)
    continueBtn = driver.find_element(By.XPATH, os.edit_info_continue_btn)
    cf.click_element(driver, continueBtn, 10)
    msg = driver.find_element(By.XPATH, os.ac_update_alert)
    time.sleep(5)
    actual_text = msg.text
    print(actual_text)
    cf.assert_element_text(msg, "Success: Your account has been successfully updated.")
    time.sleep(5)
