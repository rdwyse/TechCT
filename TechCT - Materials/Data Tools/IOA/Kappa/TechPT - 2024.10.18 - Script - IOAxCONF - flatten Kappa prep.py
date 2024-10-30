import pandas as pd
import os
from tkinter import filedialog, Tk

# Hide the root window
Tk().withdraw()

# Open a file dialog to specify the input file
print("Please select the input CSV file.")
input_file_path = filedialog.askopenfilename(title="Select Input CSV File")
# Check if a file was selected
if not input_file_path:
    print("No file selected. Exiting script.")
    exit()

# Generate output file name based on the input file name
input_file_name = os.path.basename(input_file_path)
output_file_name = os.path.splitext(input_file_name)[0] + '_collapsed_IOAxCONF.csv'

# Load the selected CSV file into a DataFrame
loadedCSV_data = pd.read_csv(input_file_path)

# Ensure the relevant columns are strings for merging and manipulation purposes
for col in ['CaregiverID', 'StudyPhase', 'SessionType', 'SessionCount', 'Merge_TotalSessionTrials', 'SessionBlockCount', 'IOAxCONF_Key']:
    loadedCSV_data[col] = loadedCSV_data[col].astype(str)

# Separate the IOA and Confederate rows based on 'Respondent'
ioa_data = loadedCSV_data[loadedCSV_data['Respondent'] == '2_IOA']
confederate_data = loadedCSV_data[loadedCSV_data['Respondent'] == '1_CONF']

# Merging IOA and Confederate data based on the matching key 'IOAxCONF_Key'
merged_data = pd.merge(
    ioa_data,
    confederate_data,
    on='IOAxCONF_Key',
    suffixes=('_IOA', '_Conf')
)

# Creating the final collapsed dataset
collapsed_data = []

# Iterating over the merged rows to collapse data
for _, row in merged_data.iterrows():
    collapsed_row = {}

    # Use relevant fields from the 1_CONF row
    collapsed_row['InstanceID'] = row['InstanceID_Conf']
    collapsed_row['CaregiverID'] = row['CaregiverID_Conf']
    collapsed_row['StudyPhase'] = row['StudyPhase_Conf']
    collapsed_row['SessionType'] = row['SessionType_Conf']
    collapsed_row['SessionCount'] = row['SessionCount_Conf']
    collapsed_row['Merge_TotalSessionTrials'] = row['Merge_TotalSessionTrials_Conf']
    collapsed_row['SessionBlockCount'] = row['SessionBlockCount_Conf']
    collapsed_row['DateTimeStamp'] = row['DateTimeStamp_Conf']

    # Set Respondent to 3_IOAxCONF for the merged row
    collapsed_row['Respondent'] = '3_IOAxCONF'

    # Keep both sets of monitoring columns (Confederate and IOA)
    for prefix, suffix in [('Conf', '_Conf'), ('IOA', '_IOA')]:
        for col in [
            'SelfMonitoring1', 'SelfMonitoring2', 'SelfMonitoring3', 'SelfMonitoring4',
            'SelfMonitoring5', 'SelfMonitoring6', 'SelfMonitoring6a_1', 'SelfMonitoring6a_2', 'SelfMonitoring6a_3',
            'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4',
            'ConfMonitoring5', 'ConfMonitoring6', 'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3',
            'ConfConfederateInteraction', 'ConfTrialNote',
            'IOAMonitoring1', 'IOAMonitoring2', 'IOAMonitoring3', 'IOAMonitoring4',
            'IOAMonitoring5', 'IOAMonitoring6', 'IOAMonitoring6a_1', 'IOAMonitoring6a_2', 'IOAMonitoring6a_3',
            'IOAConfederateInteraction', 'IOATrialNote'
        ]:
            column_name = f"{col}{suffix}"
            if column_name in row:
                collapsed_row[column_name] = row[column_name]

    # Keep the IOAxCONF_Key
    collapsed_row['IOAxCONF_Key'] = row['IOAxCONF_Key']

    # Append the collapsed row to the final data list
    collapsed_data.append(collapsed_row)

# Convert collapsed data to a DataFrame
collapsed_data_df = pd.DataFrame(collapsed_data)
    
# Save the collapsed dataset to a CSV file
collapsed_data_df.to_csv(output_file_name, index=False)

print(f"Collapsed IOAxCONF dataset saved to {output_file_name}")
