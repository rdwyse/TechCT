# Import necessary libraries
import pandas as pd
import os
from tkinter import Tk, simpledialog
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Create a file dialog for selecting the input CSV file
Tk().withdraw()  # We don't want a full GUI, so keep the root window from appearing
input_file_path = askopenfilename(title="Select the input CSV file", filetypes=[("CSV files", "*.csv")])

# Verify if the user selected a file
if not input_file_path:
    raise Exception("No input file selected.")

# Create a dialog box for the user to select respondent comparison
respondent_choice = simpledialog.askstring("Respondent Comparison", "Enter respondent comparison option (1-4):\n1: IOA and CONF\n2: IOA and CARE\n3: CONF and CARE\n4: CONF, CARE, and IOA")

# Verify if the user made a choice
if respondent_choice not in ['1', '2', '3', '4']:
    raise Exception("Invalid respondent choice.")

# Generate output file name based on the input file name
input_file_name = os.path.basename(input_file_path)
comparison_label = ''
if respondent_choice == '1':
    comparison_label = 'IOAxCONF_Key'
elif respondent_choice == '2':
    comparison_label = 'IOAxCARE_Key'
elif respondent_choice == '3':
    comparison_label = 'CONFxCARE_Key'
elif respondent_choice == '4':
    comparison_label = 'CONFxCARExIOA_Key'
output_file_name = os.path.splitext(input_file_name)[0] + '_' + comparison_label + '_RawAgreement.csv'
output_file_path = os.path.join(os.path.dirname(input_file_path), output_file_name)

# Load the selected CSV file into a DataFrame
loadedCSV_data = pd.read_csv(input_file_path)

# Ensure all columns are in the same order
output_columns = [
    'InstanceID', 'DateTimeStamp', 'Respondent', 'CaregiverID', 'StudyPhase',
    'SessionType', 'SessionCount', 'Merge_TotalSessionTrials', 'SessionBlockCount',
    'SelfMonitoring1', 'SelfMonitoring2', 'SelfMonitoring3', 'SelfMonitoring4',
    'SelfMonitoring5', 'SelfMonitoring6a_1', 'SelfMonitoring6a_2', 'SelfMonitoring6a_3',
    'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4',
    'ConfMonitoring5', 'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3',
    'ConfConfederateInteraction', 'ConfTrialNote', 'IOAMonitoring1', 'IOAMonitoring2',
    'IOAMonitoring3', 'IOAMonitoring4', 'IOAMonitoring5', 'IOAMonitoring6a_1',
    'IOAMonitoring6a_2', 'IOAMonitoring6a_3', 'IOAConfederateInteraction',
    'IOATrialNote', 'IOAxCARE_Key', 'CONFxCARE_Key', 'IOAxCONF_Key', 'CONFxCARExIOA_Key'
]

# Ensure all output columns are present, adding missing columns if necessary
for col in output_columns:
    if col not in loadedCSV_data.columns:
        loadedCSV_data[col] = pd.NA

# Reorder columns
loadedCSV_data = loadedCSV_data[output_columns]

# Ensure consistent data types for non-monitoring columns
loadedCSV_data['DateTimeStamp'] = pd.to_datetime(loadedCSV_data['DateTimeStamp'], errors='coerce')

# Convert columns to appropriate data types while keeping <NA> values
loadedCSV_data = loadedCSV_data.astype({
    'InstanceID': 'str', 'Respondent': 'str', 'CaregiverID': 'str', 'StudyPhase': 'str',
    'SessionType': 'str', 'SessionCount': 'float64', 'Merge_TotalSessionTrials': 'float64',
    'SessionBlockCount': 'float64', 'ConfMonitoring1': 'float64', 'ConfMonitoring2': 'float64',
    'ConfMonitoring3': 'float64', 'ConfMonitoring4': 'float64', 'ConfMonitoring5': 'float64',
    'ConfMonitoring6a_1': 'float64', 'ConfMonitoring6a_2': 'float64', 'ConfMonitoring6a_3': 'float64',
    'ConfConfederateInteraction': 'str', 'ConfTrialNote': 'str',
    'IOAMonitoring1': 'float64', 'IOAMonitoring2': 'float64', 'IOAMonitoring3': 'float64',
    'IOAMonitoring4': 'float64', 'IOAMonitoring5': 'float64', 'IOAMonitoring6a_1': 'float64',
    'IOAMonitoring6a_2': 'float64', 'IOAMonitoring6a_3': 'float64', 'IOAConfederateInteraction': 'str',
    'IOATrialNote': 'str', 'IOAxCARE_Key': 'str', 'CONFxCARE_Key': 'str', 'IOAxCONF_Key': 'str',
    'CONFxCARExIOA_Key': 'str'
}, errors='ignore')

# Create a new DataFrame to store comparison results
comparison_results = []

# Iterate over each row in the loaded data to append the results
for idx, row in loadedCSV_data.iterrows():
    # Create a dictionary from the row to start
    row_dict = row.to_dict()

    # List of columns to be compared between SelfMonitoring and IOA
    monitoring_columns = [
        'SelfMonitoring1', 'SelfMonitoring2', 'SelfMonitoring3', 'SelfMonitoring4', 
        'SelfMonitoring5', 'SelfMonitoring6a_1', 'SelfMonitoring6a_2', 'SelfMonitoring6a_3'
    ]

    # Loop over each SelfMonitoring and IOA pair to compare
    for col in monitoring_columns:
        conf_col = col.replace('SelfMonitoring', 'ConfMonitoring')  # Corresponding CONF column
        ioa_col = col.replace('SelfMonitoring', 'IOAMonitoring')  # Corresponding IOA column

        # Initialize monitoring result for this pair
        monitor_result = None

        # Compare SelfMonitoring and IOA columns
        conf_value = row[conf_col]
        ioa_value = row[ioa_col]

        # Check for agreement or disagreement, handle NaN values explicitly
        if pd.notna(conf_value) and pd.notna(ioa_value):
            if conf_value == ioa_value:
                if conf_value == 0:
                    monitor_result = 'D'  # Negative agreement
                elif conf_value == 1:
                    monitor_result = 'A'  # Positive agreement
            else:
                if conf_value == 1:
                    monitor_result = 'B'  # False Positive: Confederate 1, IOA 0
                elif conf_value == 0:
                    monitor_result = 'C'  # False Negative: Confederate 0, IOA 1
        else:
            monitor_result = pd.NA  # Handle missing data

        # Append result to the row dictionary
        row_dict[col.replace('Self', '')] = monitor_result

    # Append the modified row dictionary to comparison_results
    comparison_results.append(row_dict)

# Create a DataFrame from the comparison results
comparison_results_df = pd.DataFrame(comparison_results)

# Save the comparison results to a CSV file
comparison_results_df.to_csv(output_file_path, index=False)

print(f"Comparison results saved to {output_file_path}")
