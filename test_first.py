"""
Basic test
"""
#import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



URL = 'https://testqastudio.me/'

def test_smoke(browser):
    """
    SMK-1.Smoke test
    """

    browser.get(url=URL)

    element = browser.find_element(by=By.CSS_SELECTOR, value='[class*="post-11338"]')
    element.click()

    sku = browser.find_element(by=By.CSS_SELECTOR, value='[class="sku"]')

    assert sku.text == 'C3FC1BHBI4', 'Unexpected SKU for "АЙША Барный стул"'

def test_count_of_all_products(browser):
        """
        Test case TC-3
        """
        browser.get(url=URL)

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        WebDriverWait(browser, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "razzi-posts__found-inner"), "Показано 17 из 17 товары"))
        
        elements = browser.find_elements(by=By.CSS_SELECTOR, value="[id='rz-shop-content'] ul li")

        assert len(elements) == 17, "Unexpected count products"