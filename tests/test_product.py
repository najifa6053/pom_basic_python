from pages.inventory_page import Inventory
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    
    inventory = Inventory(driver)
    current_url = inventory.current_url

    assert "inventory" in driver.current_url, "Login failed or did not navigate to inventory page"
    
    product_page = ProductPage(driver)
    product_page.click_add_to_cart()

    