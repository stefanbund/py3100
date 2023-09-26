import csv
import random

# List of US state names
us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "New Hampshire", "New Jersey", "New Mexico", "New York",
    "North Carolina", "North Dakota", "Ohio", "Oklahoma",
    "Oregon", "Pennsylvania", "Rhode Island",
    "South Carolina", "South Dakota",
    "Tennessee", "Texas",
    # ... and more
]

# Randomly assign a number of stores per state until the total of 1,335 is reached
num_stores = 1335
stores = []
while len(stores) < num_stores:
    state = random.choice(us_states)
    stores.append(f"{state} {random.randint(1, 9999)}")

# Write the list of stores to a CSV file
with open("ProductSalesBuilder.csv", mode="w") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name"] + stores)
    for i in range(200000):
        product_name = f"Product {i}"
        sales_totals = [random.randint(0, 1000) for _ in range(num_stores)]
        writer.writerow([product_name] + sales_totals)

print("The list of stores has been written to 'ProductSalesBuilder.csv'.")
