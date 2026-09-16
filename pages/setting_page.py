from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json

with open("config/config.json") as f:
    config = json.load(f)

class SettingsSetup:

    setting_attribute_allowAdd_toogle = (By.ID, "allow-add-additional-attribute")

    def __init__(self, driver,wait):
        self.driver = driver
        self.wait = wait

    def go_to_settings(self):
        self.wait.until(
            EC.url_contains("/dashboard")
        )
        self.driver.get(config['setting_url'])

    def toggle_attribute_addition_allow(self):
        self.go_to_settings()
        toggle = self.wait.until(
            EC.presence_of_element_located(
                (self.setting_attribute_allowAdd_toogle)
            )
        )
        if not toggle.is_selected():
            toggle.click()
        