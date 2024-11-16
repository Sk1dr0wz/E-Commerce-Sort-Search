import csv
from product import Product

def read_products(filename):
    """Read products from a CSV file and return a list of Product objects."""
    products = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = Product(
                    row['Product ID'],
                    row['Product Name'],
                    row['Price'],
                    row['Number of Reviews'],
                    row['Rating'],
                    row['Category']
                )
                products.append(product)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Starting with an empty product list.")
    return products

def write_products(filename, products):
    """Write a list of Product objects to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Product ID', 'Product Name', 'Price', 'Number of Reviews', 'Rating', 'Category']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow({
                'Product ID': product.product_id,
                'Product Name': product.product_name,
                'Price': product.price,
                'Number of Reviews': product.number_of_reviews,
                'Rating': product.rating,
                'Category': product.category
            })
