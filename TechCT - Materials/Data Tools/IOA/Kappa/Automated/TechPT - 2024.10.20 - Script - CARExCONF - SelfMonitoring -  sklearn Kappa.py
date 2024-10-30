import pandas as pd
from sklearn.metrics import cohen_kappa_score
from tkinter import filedialog
from tkinter import Tk
import numpy as np

# Hide the root window
Tk().withdraw()

# Load the dataset
file_path = filedialog.askopenfilename(title="Select CSV File")
df = pd.read_csv(file_path)

# Print the headers to verify alignment with the script
print("Dataset Headers:")
print(df.columns.tolist())

# Print the total number of rows in the dataset
print(f"Total number of rows in the dataset: {len(df)}")

# Filter the dataset to include only rows with StudyPhase equal to '3_T3'
df = df[df['StudyPhase'] == '3_T3']

# Print the total number of rows in the filtered dataset
print(f"Total number of rows in the filtered dataset: {len(df)}")

# Set specific types for utilized columns
df = df.astype({
    'ConfMonitoring1': 'float64', 'ConfMonitoring2': 'float64', 'ConfMonitoring3': 'float64',
    'ConfMonitoring4': 'float64', 'ConfMonitoring5': 'float64', 'ConfMonitoring6': 'float64',
    'ConfMonitoring6a_1': 'float64', 'ConfMonitoring6a_2': 'float64', 'ConfMonitoring6a_3': 'float64', 
    'SelfMonitoring1': 'float64', 'SelfMonitoring2': 'float64', 'SelfMonitoring3': 'float64',
    'SelfMonitoring4': 'float64', 'SelfMonitoring5': 'float64', 'SelfMonitoring6': 'float64',
    'SelfMonitoring6a_1': 'float64', 'SelfMonitoring6a_2': 'float64', 'SelfMonitoring6a_3': 'float64',
    'CaregiverID': 'str', 'StudyPhase': 'str'
}, errors='ignore')

# Define the monitoring columns
conf_rater_columns = [
    'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4',
    'ConfMonitoring5', 'ConfMonitoring6', 'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3'
]

self_rater_columns = [
    'SelfMonitoring1', 'SelfMonitoring2', 'SelfMonitoring3', 'SelfMonitoring4',
    'SelfMonitoring5', 'SelfMonitoring6', 'SelfMonitoring6a_1', 'SelfMonitoring6a_2', 'SelfMonitoring6a_3'
]

# Flatten the observations from all columns into two single arrays, ignoring NaNs for calculations
rater1_all = df[conf_rater_columns].to_numpy().flatten()
rater2_all = df[self_rater_columns].to_numpy().flatten()

# Print the number of elements before removing NaNs
print(f"Number of elements before removing NaNs: Rater1: {len(rater1_all)}, Rater2: {len(rater2_all)}")

# Remove NaN values if present
mask = ~np.isnan(rater1_all) & ~np.isnan(rater2_all)
rater1_all = rater1_all[mask]
rater2_all = rater2_all[mask]

# Print the number of elements after removing NaNs
print(f"Number of elements after removing NaNs: Rater1: {len(rater1_all)}, Rater2: {len(rater2_all)}")

# Check if there are sufficient observations for calculations
if len(rater1_all) > 0 and len(rater2_all) > 0:
    # Calculate Cohen's Kappa for the entire set
    kappa = cohen_kappa_score(rater1_all, rater2_all)
    percent_agreement = np.mean(rater1_all == rater2_all)
    num_observations = len(rater1_all)

    results = []
    results.append(["Entire Set", kappa, percent_agreement * 100, num_observations])

    print(f"Cohen's Kappa for the entire set: {kappa}")
    print(f"Percentage Agreement for the entire set: {percent_agreement * 100:.2f}%")
    print(f"Number of observations for the entire set: {num_observations}")
else:
    print("No valid observations available for the entire set calculation.")
    results = []

# Loop through all pairs of Confederate and SelfMonitoring raters to calculate Cohen's Kappa for each pair
for conf_col, self_col in zip(conf_rater_columns, self_rater_columns[:len(conf_rater_columns)]):
    rater1 = df[conf_col]
    rater2 = df[self_col]
    
    # Remove NaN values
    mask = ~rater1.isna() & ~rater2.isna()
    rater1 = rater1[mask]
    rater2 = rater2[mask]
    
    if len(rater1) > 0 and len(rater2) > 0:
        kappa = cohen_kappa_score(rater1, rater2)
        percent_agreement = np.mean(rater1 == rater2)
        num_observations = len(rater1)
        results.append([f"{conf_col} vs {self_col}", kappa, percent_agreement * 100, num_observations])
        print(f"Cohen's Kappa between {conf_col} and {self_col}: {kappa}")
        print(f"Percentage Agreement between {conf_col} and {self_col}: {percent_agreement * 100:.2f}%")
        print(f"Number of observations between {conf_col} and {self_col}: {num_observations}")
    else:
        print(f"No valid observations available for {conf_col} vs {self_col}.")

# Split the dataset by CaregiverID and StudyPhase and calculate Cohen's Kappa for each subset
for (caregiver_id, study_phase), group in df.groupby(['CaregiverID', 'StudyPhase']):
    rater1_all = group[conf_rater_columns].to_numpy().flatten()
    rater2_all = group[self_rater_columns[:len(conf_rater_columns)]].to_numpy().flatten()

    # Remove NaN values if present
    mask = ~np.isnan(rater1_all) & ~np.isnan(rater2_all)
    rater1_all = rater1_all[mask]
    rater2_all = rater2_all[mask]

    # Print the number of elements in the subset after removing NaNs
    print(f"Subset CaregiverID {caregiver_id}, StudyPhase {study_phase}: Number of elements after removing NaNs: Rater1: {len(rater1_all)}, Rater2: {len(rater2_all)}")

    if len(rater1_all) > 0 and len(rater2_all) > 0:
        # Calculate Cohen's Kappa for the subset
        kappa = cohen_kappa_score(rater1_all, rater2_all)
        percent_agreement = np.mean(rater1_all == rater2_all)
        num_observations = len(rater1_all)
        results.append([f"CaregiverID {caregiver_id}, StudyPhase {study_phase}", kappa, percent_agreement * 100, num_observations])
        print(f"Cohen's Kappa for CaregiverID {caregiver_id}, StudyPhase {study_phase}: {kappa}")
        print(f"Percentage Agreement for CaregiverID {caregiver_id}, StudyPhase {study_phase}: {percent_agreement * 100:.2f}%")
        print(f"Number of observations for CaregiverID {caregiver_id}, StudyPhase {study_phase}: {num_observations}")
    else:
        print(f"No valid observations available for CaregiverID {caregiver_id}, StudyPhase {study_phase}.")

# Export results to a CSV file
if results:
    results_df = pd.DataFrame(results, columns=["Section", "Cohen's Kappa", "Percentage Agreement (%)", "Number of Observations"])
    output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Save Results CSV")
    if output_file_path:
        results_df.to_csv(output_file_path, index=False)
        print(f"Results saved to {output_file_path}")
else:
    print("No results to save.")
