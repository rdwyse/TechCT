# Loading the updated spreadsheet to start from scratch
import pandas as pd
import os
from tkinter import filedialog
from tkinter import Tk

# Hide the root window
Tk().withdraw()

# Open a file dialog to specify the input file
input_file_path = filedialog.askopenfilename(title="Select Input CSV File")

# Generate output file name based on the input file name
input_file_name = os.path.basename(input_file_path)
output_file_name = os.path.splitext(input_file_name)[0] + '_keyed.csv'

# Open a file dialog to specify the output directory
output_dir = filedialog.askdirectory(title="Select Output Directory")
output_file_path = os.path.join(output_dir, output_file_name)

# Load the dataset
# Read the CSV file into a DataFrame
loadedCSV_data = pd.read_csv(input_file_path)

# Convert relevant columns to strings to ensure proper matching
# Ensuring all relevant columns are strings to avoid type mismatch issues during merge
for col in ['Respondent', 'CaregiverID', 'StudyPhase', 'SessionType']:
    loadedCSV_data[col] = loadedCSV_data[col].astype(str)

# Separate the IOA and Confederate rows based on 'Respondent'
# Splitting the dataset into IOA and Confederate subsets for later merging
ioa_data = loadedCSV_data[loadedCSV_data['Respondent'] == '2_IOA']
confederate_data = loadedCSV_data[loadedCSV_data['Respondent'] == '1_CONF']

# We now want to add a unique key for each matching pair based on the specified columns:
# CaregiverID, StudyPhase, SessionType, SessionCount, Merge_TotalSessionTrials

# Merging IOA and Confederate data based on the matching columns
# Merging IOA and Confederate rows on common identifiers to create matched pairs
merged_IOAxCONF = pd.merge(
    ioa_data, 
    confederate_data, 
    on=['CaregiverID', 'StudyPhase', 'SessionType', 'SessionCount', 'Merge_TotalSessionTrials'], 
    suffixes=('_IOA', '_Conf')
)

# Creating unique keys for each match
# Generating a unique identifier for each pair of merged rows
merged_IOAxCONF['IOAxCONF_Key'] = list(range(1, len(merged_IOAxCONF) + 1))

# Merging the new keys back into the original dataset to ensure every row stays the same but with the new key
# Adding the unique keys back into the original dataset, ensuring all rows are retained
final_data_with_keys = pd.merge(loadedCSV_data, merged_IOAxCONF[['CaregiverID', 'StudyPhase', 'SessionType', 'SessionCount', 'Merge_TotalSessionTrials', 'IOAxCONF_Key']], how='left', on=['CaregiverID', 'StudyPhase', 'SessionType', 'SessionCount', 'Merge_TotalSessionTrials'])

# Save the updated dataframe to a new CSV file
# Saving the final dataset with the new keys to a CSV file
final_data_with_keys.to_csv(output_file_path, index=False)

print(f"Data with unique keys saved to {output_file_path}")
