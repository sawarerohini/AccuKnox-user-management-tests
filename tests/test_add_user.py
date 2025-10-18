from Pages.login_page import LoginPage
from Pages.admin_page import AdminPage

def test_add_user(setup):
    driver = setup
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    admin = AdminPage(driver)
    admin.navigate_to_admin()

    admin.add_user(
        role="ESS",
        status="Enabled",
        emp_name="Ranga  Akunuri",
        username="test_user1234",
        password="Test@123"
    )

    # Verify success
    success_message = admin.get_text(admin.success_msg)
    assert "success" in success_message.lower(), f"Expected success toast, got: {success_message}"
