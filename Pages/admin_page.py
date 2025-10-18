from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.success_msg = (By.XPATH, "//div[contains(@class,'oxd-toast-content')]")

    def navigate_to_admin(self):
        admin_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']")))
        admin_menu.click()
        # Wait for the Add button to ensure Admin page loaded
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Add']")))
        time.sleep(1)

    def open_add_user_form(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))).click()

    def select_user_role(self, role_name):
        role_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='User Role']/following::div[1]")))
        role_dropdown.click()
        role_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@role='listbox']//span[text()='{role_name}']")))
        role_option.click()

    def enter_employee_name(self, employee_name):
        emp_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Employee Name']/following::input[1]")))
        emp_input.clear()
        emp_input.send_keys(employee_name)
        # Select first suggestion
        suggestion = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='listbox']//span")))
        suggestion.click()

    def enter_username(self, username):
        user_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Username']/following::input[1]")))
        user_input.clear()
        user_input.send_keys(username)

    def select_status(self, status_name):
        status_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Status']/following::div[1]")))
        status_dropdown.click()
        status_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@role='listbox']//span[text()='{status_name}']")))
        status_option.click()

    def enter_passwords(self, password):
        pwd = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Password']/following::input[1]")))
        conf_pwd = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Confirm Password']/following::input[1]")))
        pwd.clear()
        conf_pwd.clear()
        pwd.send_keys(password)
        conf_pwd.send_keys(password)

    def save_user(self):
        save_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))
        save_btn.click()
        time.sleep(2)

    def add_user(self, role, status, emp_name, username, password):
        self.open_add_user_form()
        self.select_user_role(role)
        self.enter_employee_name(emp_name)
        self.enter_username(username)
        self.select_status(status)
        self.enter_passwords(password)
        self.save_user()

    def search_user(self, username):
        # Safe: ensure Admin page is open
        self.navigate_to_admin()
        search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Username']/following::input[1]")))
        search_input.clear()
        search_input.send_keys(username)
        search_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']")))
        search_btn.click()
        time.sleep(2)

    def click_edit_user(self, username):
        self.navigate_to_admin()
        edit_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[text()='{username}']/ancestor::div[@role='row']//i[@class='oxd-icon bi-pencil-fill']")))
        edit_btn.click()

    def delete_user(self, username):
        self.navigate_to_admin()
        delete_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[text()='{username}']/ancestor::div[@role='row']//i[@class='oxd-icon bi-trash']")))
        delete_btn.click()
        confirm_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes, Delete']")))
        confirm_btn.click()
        time.sleep(2)

    def get_text(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).text
        except:
            return ""
