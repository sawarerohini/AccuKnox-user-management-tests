from Pages.login_page import LoginPage
from Pages.admin_page import AdminPage

def test_validate_user(setup):
    driver = setup
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    admin = AdminPage(driver)
    admin.navigate_to_admin()
    admin.search_user("test_user1234")
    assert "test_user1234" in driver.page_source
