# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 23:59:57 2023

@author: mahesh
"""

import pytest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()


def excel_read():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    excelsheet_path = os.path.join(current_dir, 'input_datasheet.xlsx')

    try:
        df = pd.read_excel(excelsheet_path, sheet_name='Sheet1', dtype=object).fillna("")
    except FileNotFoundError as e:
        print(f"File not found: {excelsheet_path}")
        return

    for index, row in df.iterrows():
        flag = row["Flag"]
        try:
            if flag == 'Y':
                yield row
        except Exception as e:
            print(f"Exception: {e} occurred at index {index}")
            raise  # Re-raise the exception if needed


@pytest.fixture(params=excel_read())
def data(request):
    return request.param


@pytest.fixture
def login(data):
    driver.get(data['URL'])
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='My Account']")))
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']")))
    driver.find_element(By.XPATH, "//a[text()='Login']").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "input-email")))
    driver.find_element(By.ID, "input-email").send_keys(data['Username'])
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "input-password")))
    driver.find_element(By.ID, "input-password").send_keys(data['Password'])
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
