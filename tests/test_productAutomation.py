import json

from pages.login_page import LoginPage
from pages.menu_product import ProductMenu
from pages.create_product_page import CreateProduct
from pages.setting_page import SettingsSetup
from utils.excel_utils import get_products_from_excel
from utils.category_attribute_map import CATEGORY_ATTRIBUTE_MAP


with open("config/config.json") as f:
    config = json.load(f)


def test_createProduct(driver, wait):

    login_page = LoginPage(driver, wait)
    setup_attribute_setting = SettingsSetup(driver, wait)
    product_menu_page = ProductMenu(driver, wait)
    create_product_page = CreateProduct(driver, wait)

    login_page.login(config["username"], config["password"])
    setup_attribute_setting.toggle_attribute_addition_allow()
    product_menu_page.go_to_productmenu()

    products = get_products_from_excel(config["product_list"])

    for product in products:
        category = product.get("Product Category")
        column_map = CATEGORY_ATTRIBUTE_MAP.get(category, {})

        attributes = {
            # ui_label will give value of the column header for e.g name : Pearl...
            ui_label: product.get(excel_col)
            for excel_col, ui_label in column_map.items()
        }

        create_product_page.create_product(
            product_name=product["Name Of Item"],
            product_sku=product["SKU"],
            group_name=product["Group Name"],
            attributes=attributes
        )