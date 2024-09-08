from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import sys


def test_scores_service(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())

    with webdriver.Chrome(service=service, options=chrome_options) as driver:
        driver.get(url)
        try:
            score = int(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'score'))).text)
            return 1 <= score <= 1000
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

def main_function(url):
    if test_scores_service(url):
        sys.exit(0)
    else:
        sys.exit(123)#fortest