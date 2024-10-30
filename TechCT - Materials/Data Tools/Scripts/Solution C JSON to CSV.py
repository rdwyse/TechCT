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

# Define the desired header order, including IOA fields
desired_field_order = [
    "InstanceID", "EventNote", "DateTimeStamp:", "ResponseIDx", "CaregiverID", "Respondent", "StudyPhase",
    "SessionType", "SessionCount", "TotalSessionTrials", "SessionBlockCount", "TrialDirection", "CareDirStart",
    "CareDirEnd", "SelfMonitoring1", "SelfMonitoring2", "SelfMonitoring3", "SelfMonitoring4", "SelfMonitoring5",
    "SelfMonitoring6", "SelfMonitoring6a_1", "SelfMonitoring6a_2", "SelfMonitoring6a_3", "ConfResponse",
    "ConfMonitoring1", "ConfMonitoring2", "ConfMonitoring3", "ConfMonitoring4", "ConfMonitoring5", "ConfMonitoring6",
    "ConfMonitoring6a_1", "ConfMonitoring6a_2", "ConfMonitoring6a_3", "ConfChildResponse", "ConfederateInteraction",
    "ConfTrialNote", "ConfSessionNote",
    # IOA-specific fields
    "IOAVideoName", "IOADirStart", "IOADirEnd", "IOAMonitoring1", "IOAMonitoring2", "IOAMonitoring3",
    "IOAMonitoring4", "IOAMonitoring5", "IOAMonitoring6", "IOAMonitoring6a_1", "IOAMonitoring6a_2",
    "IOAMonitoring6a_3", "IOAResponse", "IOAChildResponse", "IOAConfederateInteraction", "IOATrialNote", 
    "IOASessionNote"
]

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
    # Create a CSV writer object using the desired header order
    writer = csv.DictWriter(file, fieldnames=desired_field_order)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    for obj in parsed_json_data:
        # Write each row; missing fields will automatically be handled as empty
        writer.writerow({field: obj.get(field, '') for field in desired_field_order})

print(f"Data exported to {output_file} successfully.")
