import random
import pandas as pd

# List of 25 major makeup brands
makeup_brands = [
    "Armani Beauty", "Jones Road", "Hourglass", "Fenty Beauty", "L’Oréal Paris",
    "Pat McGrath Labs", "Kosas", "Exa by Credo Beauty", "NARS Cosmetics",
    "Charlotte Tilbury", "Urban Decay", "Estee Lauder", "L’Oreal",
    "Maybelline New York", "Guerlain", "NARS", "Laura Mercier", "Chanel",
    "Clarins"
]

# List of 25 major types of makeup product types
makeup_product_types = [
    "Face Primer", "Foundation", "Concealer", "Powder", "Blush",
    "Highlighter", "Bronzer", "Eyebrow", "Eyeshadow", "Eyeliner",
    "Eye primer", "False lashes", "Eyelash glue", "Mascara",
    "Lipstick", "Lip gloss", "Lip liner", "Lip balm",
    "Setting spray", "Contour", "Setting powder",
    "Tinted moisturizer", "BB Cream", "Glitter",
    "Makeup brushes"
]

# Number of products
num_products = 200000

# Randomly assign brands and product types to each product
products = []
for _ in range(num_products):
    brand = random.choice(makeup_brands)
    product_type = random.choice(makeup_product_types)
    products.append((brand, product_type))

# Create a DataFrame with columns for identifier, product type, brand, price, volume, and title
df = pd.DataFrame(products, columns=["Brand", "Product Type"])
df["Price"] = [random.uniform(1, 100) for _ in range(num_products)]
df["Volume (mL)"] = [random.uniform(1, 100) for _ in range(num_products)]
df["Title"] = [
    f"{random.choice(makeup_product_types)} {random.choice(makeup_product_types)} "
    f"{random.choice(makeup_product_types)} {random.choice(['luxurious', 'sensory'])} "
    f"{random.choice(['experience', 'indulgence'])}"
    for _ in range(num_products)
]

# Print the first few rows of the DataFrame
print(df.head())

# Output the DataFrame to a CSV file
df.to_csv("ProductList.csv")
