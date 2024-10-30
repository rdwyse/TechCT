# Import necessary libraries
import pandas as pd
import os
from tkinter import filedialog, Tk

# Hide the root window
Tk().withdraw()

# Open a file dialog to specify the input CSV file
print("Please select the CSV file to merge.")
input_file_path = filedialog.askopenfilename(title="Select CSV File to Merge", filetypes=[("CSV files", "*.csv")])

# Check if a file was selected
if not input_file_path:
    print("No file selected. Exiting script.")
    exit()

# Load the selected CSV file into a DataFrame
combined_df = pd.read_csv(input_file_path)

# Ensure all columns are in the same order
output_columns = [
    'InstanceID', 'EventNote', 'DateTimeStamp:', 'ResponseIDx', 'Respondent', 'CaregiverID', 'StudyPhase',
    'SessionType', 'SessionCount', 'Merge_TotalSessionTrials', 'SessionBlockCount', 'TrialDirection', 'CareDirStart',
    'CareDirEnd', 'SelfMonitoring1', 'SelfMonitoring2', 'SelfMonitoring3', 'SelfMonitoring4', 'SelfMonitoring5',
    'SelfMonitoring6', 'SelfMonitoring6a_1', 'SelfMonitoring6a_2', 'SelfMonitoring6a_3', 'ConfResponse',
    'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4', 'ConfMonitoring5', 'ConfMonitoring6',
    'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3', 'ConfChildResponse', 'ConfederateInteraction',
    'ConfTrialNote', 'ConfSessionNote', 'IOAVideoName', 'IOAMonitoring1', 'IOAMonitoring2', 'IOAMonitoring3',
    'IOAMonitoring4', 'IOAMonitoring5', 'IOAMonitoring6', 'IOAMonitoring6a_1', 'IOAMonitoring6a_2', 'IOAMonitoring6a_3',
    'IOAChildResponse', 'IOAConfederateInteraction', 'IOATrialNote', 'IOASessionNote', 'IOAxCARE_Key',
    'CONFxCARE_Key', 'IOAxCONF_Key', 'CONFxCARExIOA_Key'
]

# Ensure all output columns are present, adding missing columns if necessary
for col in output_columns:
    if col not in combined_df.columns:
        combined_df[col] = pd.NA

# Reorder columns
combined_df = combined_df[output_columns]

# Create a new DataFrame to store the resolved rows
resolved_df = pd.DataFrame(columns=combined_df.columns)

# Iterate through each row to handle duplicate InstanceIDs
while not combined_df.empty:
    # Take the first row and create a copy
    current_row = combined_df.iloc[0].copy()
    instance_id = current_row['InstanceID']

    # Find all rows with the same InstanceID
    duplicate_rows = combined_df[combined_df['InstanceID'] == instance_id]

    # Combine key values from duplicates into the first occurrence
    for _, duplicate_row in duplicate_rows.iterrows():
        for key_col in ['IOAxCARE_Key', 'CONFxCARE_Key', 'IOAxCONF_Key', 'CONFxCARExIOA_Key']:
            if pd.isna(current_row[key_col]) and not pd.isna(duplicate_row[key_col]):
                current_row[key_col] = duplicate_row[key_col]

    # Append the resolved row to the new DataFrame
    resolved_df = pd.concat([resolved_df, current_row.to_frame().T], ignore_index=True)

    # Drop the processed rows from the combined DataFrame
    combined_df = combined_df[combined_df['InstanceID'] != instance_id]

# Open a file dialog to specify the output directory
print("Please select the output directory.")
output_dir = filedialog.askdirectory(title="Select Output Directory")

# Generate output file name
output_file_name = 'resolved_merged_keyed_data.csv'
output_file_path = os.path.join(output_dir, output_file_name)

# Save the resolved DataFrame to a new CSV file
resolved_df.to_csv(output_file_path, index=False)

print(f"Resolved merged data saved to {output_file_path}")
