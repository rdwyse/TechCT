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
required_columns = ['DateTimeStamp', 'CaregiverID', 'SessionNumber', 'StudyPhase', 'ConfChildResponse']
if not all(col in df.columns for col in required_columns):
    print(f"Input CSV file is missing required columns. Expected columns: {required_columns}")
    print("Actual columns in the CSV file:", df.columns)
    raise ValueError("Input CSV file does not match the expected structure.")

# Translate ConfChildResponse values to the needed transformation
def translate_conf_child_response(conf_child_response):
    if conf_child_response == '0_CO':  # Compliance
        return 0.5, 0, 0  # Compliance = 0.5, Omission = 0, Commission = 0
    elif conf_child_response == '1_PO':  # Omission
        return 0, -0.5, 0  # Compliance = 0, Omission = -0.5, Commission = 0
    elif conf_child_response == '2_PC':  # Commission
        return 0, 0, -1  # Compliance = 0, Omission = 0, Commission = -1
    else:
        return 0, 0, 0  # Default to zero if no match


# Create new columns for translated values
df['0_CO_Trans'], df['1_PO_Trans'], df['2_PC_Trans'] = zip(*df['ConfChildResponse'].apply(translate_conf_child_response))

# Initialize the final DataFrame with the necessary columns
final_df = df[['DateTimeStamp', 'CaregiverID', 'SessionNumber', 'StudyPhase', '0_CO_Trans', '1_PO_Trans', '2_PC_Trans']]

# Open file dialog to save the output CSV file
output_file = filedialog.asksaveasfilename(defaultextension=".csv",
                                           filetypes=[("CSV Files", "*.csv")],
                                           title="Save CSV as")

# Export the formatted data to CSV
final_df.to_csv(output_file, index=False)
print(f"Data successfully exported to {output_file}")
