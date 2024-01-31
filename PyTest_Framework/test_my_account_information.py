
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

@pytest.mark.usefixtures("setup")
def test_home(login):
    driver = login
    driver.find_element(By.XPATH, "//i[@class='fas fa-home']").click()

@pytest.mark.usefixtures("setup")
def test_edit_my_account_info(login):
    driver = login
    WebDriverWait(driver,10)
    time.sleep(7)
    driver.find_element(By.XPATH, "//a[contains(text(),'Edit your account information')]").click()
    WebDriverWait(driver,10)
    assert driver.title == "My Account Information"
    print("title", driver.title)
    driver.find_element(By.XPATH, os.edit_info_first_name).click()
    os.edit_info_first_name.clear()
    os.edit_info_first_name.send_keys("PranilP")
    driver.find_element(By.XPATH, os.edit_info_last_name).click()
    os.edit_info_first_name.clear()
    os.edit_info_first_name.send_keys("PalseP")
    driver.find_element(By.XPATH, os.edit_info_continue_btn).click()
    assert os.edit_info_continue_btn is not None, "Element is not present on page"
    time.sleep(7)
    assert driver.title == "My Account"
    print("title", driver.title)
    msg = driver.find_element(By.XPATH, os.ac_update_alert)
    assert msg.text == " Success: Your account has been successfully updated."
    print(msg.text)