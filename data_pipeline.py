import pandas as pd

# Extract
# This reads the file you just created
data = pd.read_csv("raw_data.csv")

# Transform
# Calculating total revenue per row
data['total'] = data['quantity'] * data['price']

print("Transformation complete. Previewing data:")
print(data.head())

# Load
# This creates a new cleaned file
data.to_csv("processed_data.csv", index=False)
print("File saved as processed_data.csv")
