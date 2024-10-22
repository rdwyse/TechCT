import pandas as pd
from sklearn.metrics import cohen_kappa_score
from tkinter import filedialog
from tkinter import Tk
import numpy as np

# Hide the root window
Tk().withdraw()

# Open a file dialog to specify the CSV file
file_path = filedialog.askopenfilename(title="Select CSV File")

# Load the dataset
df = pd.read_csv(file_path)

# Set specific types for utilized columns
df = df.astype({
    'ConfMonitoring1': 'float64', 'ConfMonitoring2': 'float64', 'ConfMonitoring3': 'float64',
    'ConfMonitoring4': 'float64', 'ConfMonitoring5': 'float64', 'ConfMonitoring6a_1': 'float64',
    'ConfMonitoring6a_2': 'float64', 'ConfMonitoring6a_3': 'float64', 
    'IOAMonitoring1': 'float64', 'IOAMonitoring2': 'float64', 'IOAMonitoring3': 'float64',
    'IOAMonitoring4': 'float64', 'IOAMonitoring5': 'float64', 'IOAMonitoring6a_1': 'float64',
    'IOAMonitoring6a_2': 'float64', 'IOAMonitoring6a_3': 'float64',
    'CaregiverID': 'str', 'StudyPhase': 'str'
}, errors='ignore')

# Drop rows with NaN values in the relevant columns
df.dropna(subset=[
    'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4',
    'ConfMonitoring5', 'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3',
    'IOAMonitoring1', 'IOAMonitoring2', 'IOAMonitoring3', 'IOAMonitoring4',
    'IOAMonitoring5', 'IOAMonitoring6a_1', 'IOAMonitoring6a_2', 'IOAMonitoring6a_3'
], inplace=True)

# Exclude CaregiverID 'Case4'
df = df[df['CaregiverID'] != 'Case4']

# Flatten the observations from all columns into two single arrays
rater1_all = df[['ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4',
                 'ConfMonitoring5', 'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3']].to_numpy().flatten()

rater2_all = df[['IOAMonitoring1', 'IOAMonitoring2', 'IOAMonitoring3', 'IOAMonitoring4',
                 'IOAMonitoring5', 'IOAMonitoring6a_1', 'IOAMonitoring6a_2', 'IOAMonitoring6a_3']].to_numpy().flatten()

# Remove NaN values if present
mask = ~np.isnan(rater1_all) & ~np.isnan(rater2_all)
rater1_all = rater1_all[mask]
rater2_all = rater2_all[mask]

# Calculate Cohen's Kappa for the entire set
kappa = cohen_kappa_score(rater1_all, rater2_all)
percent_agreement = np.mean(rater1_all == rater2_all)
num_observations = len(rater1_all)

results = []
results.append(["Entire Set", kappa, percent_agreement * 100, num_observations])

print(f"Cohen's Kappa for the entire set: {kappa}")
print(f"Percentage Agreement for the entire set: {percent_agreement * 100:.2f}%")
print(f"Number of observations for the entire set: {num_observations}")

# Loop through all pairs of Confederate and IOA raters to calculate Cohen's Kappa for each pair
conf_rater_columns = [
    'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4',
    'ConfMonitoring5', 'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3'
]

ioa_rater_columns = [
    'IOAMonitoring1', 'IOAMonitoring2', 'IOAMonitoring3', 'IOAMonitoring4',
    'IOAMonitoring5', 'IOAMonitoring6a_1', 'IOAMonitoring6a_2', 'IOAMonitoring6a_3'
]

for conf_col, ioa_col in zip(conf_rater_columns, ioa_rater_columns):
    rater1 = df[conf_col]
    rater2 = df[ioa_col]
    kappa = cohen_kappa_score(rater1, rater2)
    percent_agreement = np.mean(rater1 == rater2)
    num_observations = len(rater1.dropna())
    results.append([f"{conf_col} vs {ioa_col}", kappa, percent_agreement * 100, num_observations])
    print(f"Cohen's Kappa between {conf_col} and {ioa_col}: {kappa}")
    print(f"Percentage Agreement between {conf_col} and {ioa_col}: {percent_agreement * 100:.2f}%")
    print(f"Number of observations between {conf_col} and {ioa_col}: {num_observations}")

# Split the dataset by CaregiverID and StudyPhase and calculate Cohen's Kappa for each subset
for (caregiver_id, study_phase), group in df.groupby(['CaregiverID', 'StudyPhase']):
    rater1_all = group[conf_rater_columns].to_numpy().flatten()
    rater2_all = group[ioa_rater_columns].to_numpy().flatten()

    # Remove NaN values if present
    mask = ~np.isnan(rater1_all) & ~np.isnan(rater2_all)
    rater1_all = rater1_all[mask]
    rater2_all = rater2_all[mask]

    # Calculate Cohen's Kappa for the subset
    kappa = cohen_kappa_score(rater1_all, rater2_all)
    percent_agreement = np.mean(rater1_all == rater2_all)
    num_observations = len(rater1_all)
    results.append([f"CaregiverID {caregiver_id}, StudyPhase {study_phase}", kappa, percent_agreement * 100, num_observations])
    print(f"Cohen's Kappa for CaregiverID {caregiver_id}, StudyPhase {study_phase}: {kappa}")
    print(f"Percentage Agreement for CaregiverID {caregiver_id}, StudyPhase {study_phase}: {percent_agreement * 100:.2f}%")
    print(f"Number of observations for CaregiverID {caregiver_id}, StudyPhase {study_phase}: {num_observations}")

# Export results to a CSV file
results_df = pd.DataFrame(results, columns=["Section", "Cohen's Kappa", "Percentage Agreement (%)", "Number of Observations"])
output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Save Results CSV")
if output_file_path:
    results_df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}")
