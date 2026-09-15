from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class CreateProduct:

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
        group_field.send_keys(group_value)
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
                (self.attribute_section_locator)
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",attributes_section)

        self.wait.until(
            EC.presence_of_element_located(
                (self.attribute_row_title_locator)
            )
        )


    def select_attribute(self, attribute_name, attribute_value):
        locator = (
            By.XPATH,
            f"//div[contains(@class,'pfp-kajal-attr-row')]"
            f"[.//div[contains(@class,'pfp-kajal-attr-name')][starts-with(normalize-space(.), '{attribute_name}')]]"
            f"//button[normalize-space()='{attribute_value}']"
        )

        attribute = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            attribute
        )

        self.driver.execute_script(
            "arguments[0].click();",
            attribute
        )


    def click_save(self):
        save = self.wait.until(
            EC.element_to_be_clickable(
                (self.save_button)
            )
        )
        save.click()

    def create_product(self, product_name ,product_sku, collection_name, group_name, file_path, select_attribute):
        self.enter_productName(product_name)
        self.enter_productSku(product_sku)
        self.enter_groupName(group_name)
        self.enter_collection(collection_name)

        if file_path is not None:
            self.upload_file(file_path)

        

        






    