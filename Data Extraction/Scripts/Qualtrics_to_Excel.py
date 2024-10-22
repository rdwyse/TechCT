import json
import csv
import tkinter as tk
from tkinter import filedialog
import re
import os

# Create a Tkinter root window (hidden)
root = tk.Tk()
root.withdraw()

# Open a file dialog to select the input CSV file
csv_file = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV Files", "*.csv")])

# Read the CSV data from the file
with open(csv_file, "r") as file:
    csv_reader = csv.DictReader(file)
    rows = list(csv_reader)

# Debugging: Check if the rows variable is populated
if rows:
    print(f"CSV file loaded successfully. Number of rows: {len(rows)}")
    print(f"First row: {rows[0]}")
else:
    print("The CSV file did not load correctly or is empty.")

# Initialize a list to hold all parsed JSON objects
all_parsed_json_data = []

# Loop through each row in the CSV
for row_idx, row in enumerate(rows):
    # Combine all values in the row into a single string for easier searching
    row_data = " ".join(row.values())
    
    # Search for JSON strings using the delimiters
    json_strings = re.findall(r'\[{.*?}\]', row_data, re.DOTALL)
    
    if not json_strings:
        print(f"No JSON found in row {row_idx}")
    
    for json_idx, json_string in enumerate(json_strings):
        try:
            # Clean and parse each JSON string
            cleaned_json_data = re.sub(r'\]\s*\[', ',', json_string)
            parsed_json_data = json.loads(cleaned_json_data)
            all_parsed_json_data.extend(parsed_json_data)
            print(f"Successfully parsed JSON data from row {row_idx}, entry {json_idx}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON data in row {row_idx}, entry {json_idx}: {e}")

# Extract the field names from the first JSON object
if all_parsed_json_data:
    field_names = list(all_parsed_json_data[0].keys())
else:
    field_names = []

# Get the base name of the input file with the extension
input_file_name = os.path.basename(csv_file)

# Open a file dialog to specify the output directory
output_dir = filedialog.askdirectory(title="Select Output Directory")

# Generate the output file path using the input file name
output_file = os.path.join(output_dir, input_file_name)

# Change the file extension of the output file to .csv
output_file = os.path.splitext(output_file)[0] + "_processed.csv"

# Open the output file in write mode
with open(output_file, "w", newline="") as file:
    if field_names:
        # Create a CSV writer object
        writer = csv.DictWriter(file, fieldnames=field_names)

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for obj in all_parsed_json_data:
            writer.writerow(obj)

        print(f"Data exported to {output_file} successfully.")
    else:
        print("No data to write. The CSV file will be empty.")

# Debugging end message
if not all_parsed_json_data:
    print("No JSON data was parsed from the input file. The CSV file is empty.")
