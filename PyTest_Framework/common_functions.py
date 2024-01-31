# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 11:17:00 2024

@author: mahesh
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_element(driver, element, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(element)
        )
        element.click()
        print("Element clicked successfully.")
    except Exception as e:
        print(f"Exception occurred while clicking element: {e}")


def send_keys_to_element(driver, element, keys_to_send, timeout=10):

    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of(element)
        )
        element.send_keys(keys_to_send)
        print(f"Keys '{keys_to_send}' sent to element successfully.")
    except Exception as e:
        print(f"Exception occurred while sending keys to element: {e}")


def assert_element_text(element, expected_text):
    actual_text = element.text
    assert actual_text == expected_text, f"Assertion failed: Expected '{expected_text}' but got '{actual_text}'"
    print("Assertion passed")
