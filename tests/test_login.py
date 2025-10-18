import time

from Pages.login_page import LoginPage

def test_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    time.sleep(5)
    assert "dashboard" in driver.current_url.lower()
