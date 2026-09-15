from openpyxl import load_workbook

def get_products_from_excel(file_path):
    workbook = load_workbook(file_path)
    sheet = workbook.active

    products = []

    for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, values_only=True):
        product = {
            "name" : row[0],
            "sku" : row[1],
            "category" : row[2],
            "group_name" : row[3],
            "shape" : row[4],
            "color" : row[5],
            "pearl" : row[6],
            "type" : row[7],
            "strand_type" : row[8],
            "length" : row[9],
            "size" : row[10],
        }

        if product["name"] is not None:
            products.append(product)

    print("TOTAL PRODUCTS:", len(products))
    workbook.close()
    return products
       