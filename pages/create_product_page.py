from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class CreateProduct:

    add_product_button = (By.XPATH, "//button[normalize-space()='Add product']")
    product_name =  (By.XPATH, "//input[@placeholder='e.g. Silver Ring 22K']")
    product_sku = (By.XPATH, "//input[@placeholder='e.g. RNG-22K-001']")
    collection_name = (By.CSS_SELECTOR, "input[placeholder='e.g. Summer 2026']")
    product_group = (By.CSS_SELECTOR, "input[aria-label='Product group']")
    file_input = (By.CSS_SELECTOR, "input[type='file']")
    attribute_section_locator = (By.XPATH, "//div[contains(@class,'pfp-section-title')][normalize-space()='Product Attributes']")
    attribute_row_title_locator = (By.CLASS_NAME, "pfp-kajal-attr-row")
    save_button = (By.XPATH, "//button[@type='submit']")


    def __init__(self, driver , wait):
        self.driver = driver
        self.wait = wait

    def click_add_product(self):
        add_button = self.wait.until(
            EC.element_to_be_clickable(
                (self.add_product_button)
            )
        )
        add_button.click()

    def enter_productName(self, name_value):
        name_field = self.wait.until(
            EC.visibility_of_element_located(
                (self.product_name)
            )
        )
        name_field.send_keys(name_value)

    def enter_productSku(self, sku_value):
        sku_field = self.wait.until(
            EC.visibility_of_element_located(
                (self.product_sku)
            )
        )
        sku_field.send_keys(sku_value)

    def enter_collection(self, collection_value):
        collection_field = self.wait.until(
            EC.visibility_of_element_located(
                (self.collection_name)
            )
        )
        collection_field.send_keys(collection_value)

    def enter_groupName(self, group_value):
        group_field = self.wait.until(
            EC.visibility_of_element_located(
                (self.product_group)
            )
        )
        group_field.click()
        group_field.send_keys(group_value)
        group_field.send_keys(Keys.ENTER)

    
    def upload_file(self, filepath):
        file_field = self.wait.until(
            EC.presence_of_element_located(
                (self.file_input)
            )
        )
        file_field.send_keys(filepath)

    def scrollto_attribute_section(self):

        attributes_section = self.wait.until(
            EC.presence_of_element_located(
                self.attribute_section_locator
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            attributes_section
        )

        self.wait.until(
            EC.presence_of_element_located(
                self.attribute_row_title_locator
            )
        )

        print("Attribute rows FOUND")

    def select_attribute(self, attribute_name, attribute_value):
        row_locator = (
            By.XPATH,
            f"//div[contains(@class,'pfp-kajal-attr-row')]"
            f"[.//div[contains(@class,'pfp-kajal-attr-name')][starts-with(normalize-space(.), '{attribute_name}')]]"
        )

        row = self.wait.until(EC.presence_of_element_located(row_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", row)

        button_locator = (By.XPATH, f".//button[normalize-space()='{attribute_value}']")

        try:
            attribute = self.wait.until(lambda d: row.find_element(*button_locator))
            # JS Click : Enforce click whe normal loactor click doesnot work
            self.driver.execute_script("arguments[0].click();", attribute)

        except TimeoutException:
            print(f"'{attribute_value}' not found for '{attribute_name}' — adding it")
            self.add_attribute_value(row, attribute_value)

    def add_attribute_value(self, row, attribute_value):
        add_toggle = row.find_element(By.CSS_SELECTOR, "button.pfp-kajal-add-toggle")
        self.driver.execute_script("arguments[0].click();", add_toggle)

        new_value_input = self.wait.until(
            lambda d: row.find_element(By.CSS_SELECTOR, "input")
        )
        new_value_input.send_keys(attribute_value)

        confirm_button = row.find_element(By.CSS_SELECTOR, "button.pfp-kajal-add-confirm")
        self.driver.execute_script("arguments[0].click();", confirm_button)


    def click_save(self):
        save = self.wait.until(
            EC.element_to_be_clickable(
                (self.save_button)
            )
        )
        self.driver.execute_script("arguments[0].click();", save)
       


    def create_product(self, product_name ,product_sku, group_name, attributes, collection_name=None,  file_path=None):
        self.click_add_product()
        self.enter_productName(product_name)
        self.enter_productSku(product_sku)

        if collection_name:
            self.enter_collection(collection_name)

        self.enter_groupName(group_name)

        if file_path:
            self.upload_file(file_path)

        self.scrollto_attribute_section()

        for attribute_name, attribute_value in attributes.items():
            if attribute_value:
                print(f"Selecting: {attribute_name} = {attribute_value}")
                self.select_attribute(
                    attribute_name,
                    attribute_value
                )

        self.click_save()


   