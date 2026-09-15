from selenium.webdriver.support import expected_conditions as EC
import json

with open("config/config.json") as f:
    config = json.load(f)

class ProductMenu:
    def __init__(self, driver,wait):
        self.driver = driver
        self.wait = wait

    def go_to_productmenu(self):
        self.wait.until(
            EC.url_contains("/dashboard")
        )
        self.driver.get(config['product_create_url'])

        