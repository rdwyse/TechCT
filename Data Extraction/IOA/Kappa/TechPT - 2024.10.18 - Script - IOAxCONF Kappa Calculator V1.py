# Import necessary libraries
import pandas as pd
import os

# Hard code the file path for testing
input_file_path = "D:\\OneDrive\\OneDrive - Central Michigan University\\Documents\\GitHub\\TechPT\\Data Extraction and Tables\\Scripts\\IOA\\Kappa\\TechPT - 2024.10.18 - Data - IOAxCONF_Keyed_flat.csv"

# Hard code the respondent choice for testing
respondent_choice = '1'

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
    'SelfMonitoring5', 'SelfMonitoring6', 'SelfMonitoring6a_1', 'SelfMonitoring6a_2', 
    'SelfMonitoring6a_3', 'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 
    'ConfMonitoring4', 'ConfMonitoring5', 'ConfMonitoring6', 'ConfMonitoring6a_1', 
    'ConfMonitoring6a_2', 'ConfMonitoring6a_3', 'ConfConfederateInteraction', 
    'ConfTrialNote', 'IOAMonitoring1', 'IOAMonitoring2', 'IOAMonitoring3', 
    'IOAMonitoring4', 'IOAMonitoring5', 'IOAMonitoring6', 'IOAMonitoring6a_1', 
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
    'ConfMonitoring6': 'float64', 'ConfMonitoring6a_1': 'float64', 'ConfMonitoring6a_2': 'float64', 
    'ConfMonitoring6a_3': 'float64', 'ConfConfederateInteraction': 'str', 'ConfTrialNote': 'str',
    'IOAMonitoring1': 'float64', 'IOAMonitoring2': 'float64', 'IOAMonitoring3': 'float64', 
    'IOAMonitoring4': 'float64', 'IOAMonitoring5': 'float64', 'IOAMonitoring6': 'float64', 
    'IOAMonitoring6a_1': 'float64', 'IOAMonitoring6a_2': 'float64', 'IOAMonitoring6a_3': 'float64', 
    'IOAConfederateInteraction': 'str', 'IOATrialNote': 'str', 'IOAxCARE_Key': 'str', 
    'CONFxCARE_Key': 'str', 'IOAxCONF_Key': 'str', 'CONFxCARExIOA_Key': 'str'
}, errors='ignore')

# Create a new DataFrame to store comparison results
comparison_results = []

# Iterate over each row in the loaded data to append the results
for idx, row in loadedCSV_data.iterrows():
    # Initialize monitoring result for this row
    monitor1 = None
    
    # Compare ConfMonitoring1 and IOAMonitoring1
    confmonitoring1 = row['ConfMonitoring1']
    ioamonitoring1 = row['IOAMonitoring1']
       
    # Check for agreement or disagreement, handle NaN values explicitly
    if pd.notna(confmonitoring1) and pd.notna(ioamonitoring1):
        if confmonitoring1 == ioamonitoring1:
            if confmonitoring1 == 0:
                monitor1 = 'D'  # Negative agreement
            elif confmonitoring1 == 1:
                monitor1 = 'A'  # Positive agreement
        else:
            if confmonitoring1 == 1:
                monitor1 = 'B'  # False Positive: Confederate 1, IOA 0
            elif confmonitoring1 == 0:
                monitor1 = 'C'  # False Negative: Confederate 0, IOA 1

    else:
        print(f"Skipping row {idx} due to NaN values.")

    # Create a dictionary from the row and add 'Monitoring1'
    row_dict = row.to_dict()
    row_dict['Monitoring1'] = monitor1

    # Append the modified row dictionary to comparison_results
    comparison_results.append(row_dict)

# Create a DataFrame from the comparison results
comparison_results_df = pd.DataFrame(comparison_results)

# Save the comparison results to a CSV file
comparison_results_df.to_csv(output_file_path, index=False)

print(f"Comparison results saved to {output_file_path}")