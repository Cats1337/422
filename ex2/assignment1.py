import json
import csv
from datetime import datetime

# Load data from data.json
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Filter records with a valid credit card number
filtered_data = [record for record in data if record.get('creditcard') is not None]

# Generate CSV file name with the format YYYYMMDD.csv
csv_filename = datetime.now().strftime('%Y%m%d') + '.csv'

# Write the filtered data to the CSV file
with open(csv_filename, 'w', newline='') as csv_file:
    fieldnames = ['Name', 'Credit Card']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write header
    writer.writeheader()

    # Write data
    for record in filtered_data:
        writer.writerow({'Name': record['name'], 'Credit Card': record['creditcard']})

print(f"CSV file '{csv_filename}' has been generated with valid credit card records.")
