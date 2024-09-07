import sys

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def test_scores_service(url):
    dr = webdriver.Chrome()
    dr.get(url)
    try:
        score = int(WebDriverWait(dr, 10).until(EC.presence_of_element_located((By.ID, 'score'))).text)
        return 1 <= score <= 1000
    except ValueError:
        return False


def main_function(url):
    if test_scores_service(url):
        sys.exit(0)
    else:
        sys.exit(-1)


