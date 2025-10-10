from pages.inventory_page import Inventory
from pages.login_page import LoginPage

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    
    inventory = Inventory(driver)
    current_url = inventory.current_url

    assert "inventory" in driver.current_url, "Login failed or did not navigate to inventory page"