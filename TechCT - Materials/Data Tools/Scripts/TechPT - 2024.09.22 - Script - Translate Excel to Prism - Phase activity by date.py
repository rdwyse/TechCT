# Import necessary libraries
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Hide the root window for file dialogs
root = tk.Tk()
root.withdraw()

# Open file dialog to select input CSV file
csv_file = filedialog.askopenfilename(title="Select CSV File",
                                      filetypes=[("CSV Files", "*.csv")])

# Load the CSV data with DateTimeStamp as object
df = pd.read_csv(csv_file, dtype={'DateTimeStamp': 'object'})

# Convert Excel serial date format to datetime
df['DateTimeStamp'] = pd.to_datetime(df['DateTimeStamp'].astype(float), origin='1899-12-30', unit='D', errors='coerce')

# Ensure required columns are present
required_columns = ['DateTimeStamp', 'CaregiverID', 'SessionNumber', 'StudyPhase', 'ALL_SessionType']
if not all(col in df.columns for col in required_columns):
    print(f"Input CSV file is missing required columns. Expected columns: {required_columns}")
    print("Actual columns in the CSV file:", df.columns)
    raise ValueError("Input CSV file does not match the expected structure.")

# Remove the leading two characters from 'StudyPhase' and 'ALL_SessionType'
df['StudyPhase'] = df['StudyPhase'].str.slice(2)
df['ALL_SessionType'] = df['ALL_SessionType'].str.slice(2)

# Create 'Phase_Part' by combining 'StudyPhase' and 'ALL_SessionType'
df['Phase_Part'] = df['StudyPhase'] + "_" + df['ALL_SessionType']

# Format DateTimeStamp to mm/dd/yy format
df['DateOnly'] = df['DateTimeStamp'].dt.strftime('%m/%d/%y')

# Initialize the output DataFrame
output_df = pd.DataFrame()

# Get unique DateTimeStamps for the X-axis and ensure each caregiver (Case1, Case2, Case3, Case4) is represented in the Y-axis
unique_dates = df['DateOnly'].unique()
output_df['DateTimeStamp'] = unique_dates

# Define the caregivers (Y-axis)
caregivers = ['Case1', 'Case2', 'Case3', 'Case4']

# Loop through the caregivers and fill the 'Phase_Part' information, concatenating if there are multiple entries on the same day
for caregiver in caregivers:
    caregiver_data = df[df['CaregiverID'] == caregiver]
    
    for idx, date in enumerate(unique_dates):
        # Filter the caregiver data for the current date
        filtered_rows = caregiver_data[caregiver_data['DateOnly'] == date]
        
        if not filtered_rows.empty:
            # Concatenate the Phase_Part values if there are multiple entries
            phase_part_combined = ', '.join(filtered_rows['Phase_Part'].unique())  # Use unique values
            output_df.loc[idx, caregiver] = phase_part_combined
        else:
            output_df.loc[idx, caregiver] = 'No Data'

# Now, iterate over the DataFrame and remove 'No Data' from each cell
for caregiver in caregivers:
    output_df[caregiver] = output_df[caregiver].apply(lambda x: ', '.join(set(x.split(', ')) - {'No Data'}) if isinstance(x, str) else x)

# Open file dialog to save the output CSV file
output_file = filedialog.asksaveasfilename(defaultextension=".csv",
                                           filetypes=[("CSV Files", "*.csv")],
                                           title="Save CSV as")

# Export the formatted data to CSV
output_df.to_csv(output_file, index=False)
print(f"Data successfully exported to {output_file}")
