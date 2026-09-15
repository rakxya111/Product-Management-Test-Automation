import json

from pages.login_page import LoginPage
from pages.menu_product import ProductMenu
from pages.create_product_page import CreateProduct
from utils.excel_utils import get_products_from_excel


with open("config/config.json") as f:
    config = json.load(f)


def test_createProduct(driver, wait):

    login_page = LoginPage(driver, wait)
    product_menu_page = ProductMenu(driver, wait)
    create_product_page = CreateProduct(driver, wait)

    # Login
    login_page.login(
        config["username"],
        config["password"]
    )

    # Go to Product menu
    product_menu_page.go_to_productmenu()

    # Read Excel
    products = get_products_from_excel(
        config["product_list"]
    )

    # Create each product
    for product in products:

        attributes = {
            "Shape": product["shape"],
            "Color": product["color"],
            "Pearl": product["pearl"],
            "Type": product["type"],
            "Strand Type": product["strand_type"],
            "Length (Inches)": product["length"],
            "Size mm": product["size"]
        }

        create_product_page.create_product(
            product_name=product["name"],
            product_sku=product["sku"],
            group_name=product["group_name"],
            attributes=attributes
        )