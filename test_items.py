import pytest
from selenium.webdriver.common.by import By


class TestShopItems:
    @pytest.mark.parametrize("url", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/", ])
    def test_basket_button_exists(self, browser, url: str):
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

