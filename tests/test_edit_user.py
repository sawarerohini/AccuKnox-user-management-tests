import time

from Pages.login_page import LoginPage
from Pages.admin_page import AdminPage

def test_edit_user(setup):
    driver = setup
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    admin = AdminPage(driver)
    admin.navigate_to_admin()
    admin.search_user("test_user1234")
    time.sleep(4)
    admin.click_edit_user("test_user1234")
    success_message = admin.get_text(admin.success_msg, timeout=5)
    assert "success" in success_message.lower(), f"Expected success toast, got: '{success_message}'"
