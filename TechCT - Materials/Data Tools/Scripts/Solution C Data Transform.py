import re
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root window (hidden)
root = tk.Tk()
root.withdraw()

# Open a file dialog to select the input text file
txt_file = filedialog.askopenfilename(title="Select Text File", filetypes=[("Text Files", "*.txt")])

# Read the raw data from the text file
with open(txt_file, "r") as file:
    raw_data = file.read()

# Use a regular expression to find and extract all JSON blocks
json_blocks = re.findall(r'\[.*?\]', raw_data, re.DOTALL)

# Combine all found JSON blocks into a single string for export
cleaned_json_data = ' '.join(json_blocks)

# Open a file dialog to specify the output directory
output_dir = filedialog.askdirectory(title="Select Output Directory")

# Write the cleaned JSON data to a new text file
output_file = f"{output_dir}/cleaned_json_output.txt"
with open(output_file, "w") as file:
    file.write(cleaned_json_data)

print(f"Cleaned JSON data exported to {output_file}")
