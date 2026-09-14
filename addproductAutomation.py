from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

# SETUP

LOGIN_PAGE_URL = "https://uat-kajal.danfesolution.com//login"
PRODUCT_PAGE_URL = "https://uat-kajal.danfesolution.com/inventory/products"
name = "Silver Ring 22k"
code = "PN-PE-RD-1011-SS-0001"
collection = 'Summer 2026'
group = "Jenna Flower Pearl Necklace"
catgegory = "Pearl Necklace"
email = "admin"
password = "Admin@123"
shape = 'Round'
color = 'Lavender'
pearl = 'Edision'
type = 'Strand'
strand_type = 'Single'
length = '22-23'
size = '10-11mm'


driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 15)

# LOGIN
driver.get(LOGIN_PAGE_URL)

username = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "usernameOrEmail")
    )
)
username.send_keys(email)

password_field = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "password")
    )
)
password_field.send_keys(password)

login = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")
    )
)
login.click()

# Wait until dashboard appears
wait.until(
    EC.url_contains("/dashboard")
)

# PRODUCT PAGE
driver.get(PRODUCT_PAGE_URL)


# Add product
add_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Add product']")
    )
)
add_button.click()



product_name = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='e.g. Silver Ring 22K']")
    )
)
product_name.send_keys(name)


product_sku = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='e.g. RNG-22K-001']")
    )
)
product_sku.send_keys(code)

if collection:
    collection_name = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='e.g. Summer 2026']")
        )
    )
    collection_name.send_keys(collection)

product_group = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[aria-label='Product group']")
    )
)

product_group.click()
product_group.send_keys(group)
product_group.send_keys(Keys.ENTER)

file_input = wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[type='file']")
    )
)

file_input.send_keys(r"D:/wallpaper/4.png")

virtual_product = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(@class,'pfp-toggle-row')][.//label[normalize-space()='Virtual Product']]//button[@role='switch']")
    )
)

if virtual_product.get_attribute("aria-checked") == "false":
    virtual_product.click()


# Scroll to the attributes section once, before selecting any attribute,
# so the chips are actually rendered/visible before we try to click them.
attributes_section = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//div[contains(@class,'pfp-section-title')][normalize-space()='Product Attributes']")
    )
)
driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    attributes_section
)
wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "pfp-kajal-attr-row"))
)

# DEBUG: print what attribute rows actually exist right now
rows = driver.find_elements(By.CLASS_NAME, "pfp-kajal-attr-row")
print(f"Found {len(rows)} attribute row(s):")
for r in rows:
    print(" -", r.find_element(By.CLASS_NAME, "pfp-kajal-attr-name").text)


def select_attribute(attribute_name, attribute_value):
    locator = (
        By.XPATH,
        f"//div[contains(@class,'pfp-kajal-attr-row')]"
        f"[.//div[contains(@class,'pfp-kajal-attr-name')][starts-with(normalize-space(.), '{attribute_name}')]]"
        f"//button[normalize-space()='{attribute_value}']"
    )

    element = wait.until(
        EC.presence_of_element_located(locator)
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        element
    )

    wait.until(
        EC.element_to_be_clickable(locator)
    ).click()

select_attribute("Shape", "Round")
select_attribute("Color", "Lavender")
select_attribute("Pearl", "Edision")
select_attribute("Type", "Strand")
select_attribute("Strand Type", "Single")
select_attribute("Length (Inches)", "22-23")
select_attribute("Size mm", "10-11mm")


# KEEP BROWSER OPEN
input("Press ENTER to close browser...")

driver.quit()