import pandas as pd
from sklearn.metrics import cohen_kappa_score, confusion_matrix
from tkinter import filedialog
from tkinter import Tk
import numpy as np

# Hide the root window
Tk().withdraw()

# Open a file dialog to specify the CSV file
file_path = filedialog.askopenfilename(title="Select CSV File")

# Load the dataset
df = pd.read_csv(file_path)

# Clean column names by stripping any leading or trailing spaces
df.columns = df.columns.str.strip()

# Ensure the correct columns are present
if 'ConfConfederateInteraction' not in df.columns or 'IOAConfederateInteraction' not in df.columns:
    raise KeyError("Required columns 'ConfConfederateInteraction' or 'IOAConfederateInteraction' not found in the dataset")

# Drop rows with NaN values in the relevant columns (Confederate and IOA observations)
df.dropna(subset=['ConfConfederateInteraction', 'IOAConfederateInteraction'], inplace=True)

# Flatten the Confederate and IOA interaction columns into single arrays
confederate_obs = df['ConfConfederateInteraction'].to_numpy().flatten()
ioa_obs = df['IOAConfederateInteraction'].to_numpy().flatten()

# Remove NaN values if present (this step is redundant after dropna but added for robustness)
mask = ~np.isnan(confederate_obs) & ~np.isnan(ioa_obs)
confederate_obs = confederate_obs[mask]
ioa_obs = ioa_obs[mask]

# Calculate Cohen's Kappa for the entire set, provide possible labels [0, 1] to ensure correct shape
kappa = cohen_kappa_score(confederate_obs, ioa_obs, labels=[0, 1])
percent_agreement = np.mean(confederate_obs == ioa_obs)
num_observations = len(confederate_obs)

# Generate the confusion matrix for the entire set
conf_matrix = confusion_matrix(confederate_obs, ioa_obs, labels=[0, 1])
tn, fp, fn, tp = conf_matrix.ravel() if conf_matrix.size == 4 else (conf_matrix[0, 0], 0, 0, 0)

# Initialize results list and append results for the entire set
results = []
results.append(["Entire Set", kappa, percent_agreement * 100, num_observations, tn, fp, fn, tp])

# Split the dataset by CaregiverID and StudyPhase and calculate Cohen's Kappa for each subset
for (caregiver_id, study_phase), group in df.groupby(['CaregiverID', 'StudyPhase']):
    # Extract the relevant Confederate and IOA observations
    conf_obs = group['ConfConfederateInteraction'].to_numpy().flatten()
    ioa_obs = group['IOAConfederateInteraction'].to_numpy().flatten()

    # Remove NaN values if present
    mask = ~np.isnan(conf_obs) & ~np.isnan(ioa_obs)
    conf_obs = conf_obs[mask]
    ioa_obs = ioa_obs[mask]

    # Calculate Cohen's Kappa for the subset, provide labels=[0, 1] to ensure correct shape
    if len(np.unique(conf_obs)) > 1 and len(np.unique(ioa_obs)) > 1:
        kappa = cohen_kappa_score(conf_obs, ioa_obs, labels=[0, 1])
    else:
        kappa = np.nan  # Kappa is undefined when there is no variation

    percent_agreement = np.mean(conf_obs == ioa_obs)
    num_observations = len(conf_obs)

    # Generate the confusion matrix for this subset
    conf_matrix = confusion_matrix(conf_obs, ioa_obs, labels=[0, 1])
    
    # Handle confusion matrix shape to ensure it includes all possible cases
    if conf_matrix.size == 4:
        tn, fp, fn, tp = conf_matrix.ravel()
    else:
        tn, fp, fn, tp = (conf_matrix[0, 0], 0, 0, 0) if conf_matrix.size == 1 else (0, 0, 0, 0)

    # Append results to the list
    results.append([f"CaregiverID {caregiver_id}, StudyPhase {study_phase}", kappa, percent_agreement * 100, num_observations, tn, fp, fn, tp])

# Convert results to a DataFrame with confusion matrix columns
results_df = pd.DataFrame(results, columns=["Section", "Cohen's Kappa", "Percentage Agreement (%)", "Number of Observations", "TN", "FP", "FN", "TP"])

# Prompt user to save the output file
output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Save Results CSV")
if output_file_path:
    results_df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}")
