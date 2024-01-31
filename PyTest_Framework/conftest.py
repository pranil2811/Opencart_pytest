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


@pytest.fixture(scope="class")
def setup(request):
    global driver
    edgedriver_path = r"C:\Users\mahes\Downloads\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(executable_path=edgedriver_path)
    driver.maximize_window()
    #driver.get("http://localhost/opencart/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()


def excel_read():
    excelsheet_path = r'C:\Users\mahes\.spyder-py3\PyTest_Framework\input_datasheet.xlsx'
    df = pd.read_excel(excelsheet_path,sheet_name='Sheet1',dtype=object).fillna("")

    for rows in range(df.shape[0]):
        flag = df["Flag"][rows]

        try:
            if flag == 'Y':
                yield df.iloc[rows]
        except Exception as e:
            print("Exception:-"+str(e).strip()+" of type:-"+str(type(e))+" occured")
            raise Exception(e)


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
    
    
    