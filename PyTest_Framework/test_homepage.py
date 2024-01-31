# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 23:59:57 2023

@author: mahesh
"""

from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup")
class Test_HomePage():
    
    def test_home(self,login):
        driver = self.driver
        driver.find_element(By.XPATH, "//i[@class='fas fa-home']").click()
        