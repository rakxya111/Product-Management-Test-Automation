from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    username = (By.ID, "usernameOrEmail")
    password = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def enter_username(self, username_value):
        username_field = self.wait.until(
            EC.visibility_of_element_located(
                self.username
            )
        )
        username_field.send_keys(username_value)

    def enter_password(self, password_value):
        password_field = self.wait.until(
            EC.visibility_of_element_located(
                self.password
            )
        )
        password_field.send_keys(password_value)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(
                self.login_button
            )
        )
        login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()