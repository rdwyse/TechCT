import json
import csv
import tkinter as tk
from tkinter import filedialog
import re
import os

# Create a Tkinter root window (hidden)
root = tk.Tk()
root.withdraw()

# Open a file dialog to select the input JSON file
json_file = filedialog.askopenfilename(title="Select JSON File", filetypes=[("Text Files", "*.txt")])

# Read the JSON data from the file
with open(json_file, "r") as file:
    json_data = file.read()

# Clean up the JSON data by removing the delimiter pattern
cleaned_json_data = re.sub(r'\]\s*\[', ',', json_data)

# Parse the cleaned JSON data
parsed_json_data = json.loads(cleaned_json_data)

# Extract the field names from the first object
field_names = list(parsed_json_data[0].keys())

# Get the base name of the input file with the extension
input_file_name = os.path.basename(json_file)

# Open a file dialog to specify the output directory
output_dir = filedialog.askdirectory(title="Select Output Directory")

# Generate the output file path using the input file name
output_file = os.path.join(output_dir, input_file_name)

# Change the file extension of the output file to .csv
output_file = os.path.splitext(output_file)[0] + ".csv"

# Open the output file in write mode
with open(output_file, "w", newline="") as file:
    # Create a CSV writer object
    writer = csv.DictWriter(file, fieldnames=field_names)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    for obj in parsed_json_data:
        writer.writerow(obj)

print(f"Data exported to {output_file} successfully.")