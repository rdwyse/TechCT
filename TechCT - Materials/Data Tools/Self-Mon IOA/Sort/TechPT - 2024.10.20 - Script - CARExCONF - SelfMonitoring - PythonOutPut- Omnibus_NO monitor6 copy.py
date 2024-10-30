import pandas as pd
from sklearn.metrics import cohen_kappa_score
import numpy as np
from tkinter import filedialog
from tkinter import Tk

# Hide the root window
Tk().withdraw()

# Load the dataset
file_path = filedialog.askopenfilename(title="Select CSV File")
df = pd.read_csv(file_path)

# Define the columns to be compared
conf_monitoring_columns = [
    'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4',
    'ConfMonitoring5', 'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3'
]
self_monitoring_columns = [
    'SelfMonitoring1', 'SelfMonitoring2', 'SelfMonitoring3', 'SelfMonitoring4',
    'SelfMonitoring5', 'SelfMonitoring6a_1', 'SelfMonitoring6a_2', 'SelfMonitoring6a_3'
]

# Function to calculate Cohen's Kappa and other metrics
def calculate_metrics(rater1, rater2):
    if np.all(rater1 == rater2):
        kappa = 1.0
        percent_agreement = 100.0
    else:
        kappa = cohen_kappa_score(rater1, rater2)
        percent_agreement = np.mean(rater1 == rater2) * 100
    num_observations = len(rater1)

    true_positive = np.sum((rater1 == 1) & (rater2 == 1))
    false_positive = np.sum((rater1 == 0) & (rater2 == 1))
    false_negative = np.sum((rater1 == 1) & (rater2 == 0))
    true_negative = np.sum((rater1 == 0) & (rater2 == 0))
    total_agreement_count = true_positive + true_negative
    total_observation_count = len(rater1)
    expected_agreement = (
        ((true_positive + false_negative) / total_observation_count) * ((true_positive + false_positive) / total_observation_count)
        + ((false_positive + true_negative) / total_observation_count) * ((false_negative + true_negative) / total_observation_count)
    )
    po_minus_pe = percent_agreement / 100 - expected_agreement
    one_minus_pe = 1 - expected_agreement
    k = po_minus_pe / one_minus_pe if one_minus_pe != 0 else np.nan

    return [kappa, percent_agreement, num_observations, true_positive, false_positive, false_negative, true_negative, total_agreement_count, total_observation_count, expected_agreement, po_minus_pe, one_minus_pe, k]

# Initialize results list
results = []

# Calculate metrics for each monitoring pair
for conf_col, self_col in zip(conf_monitoring_columns, self_monitoring_columns):
    # Flatten the observations from each pair of columns, ignoring NaNs for calculations
    rater1 = df[conf_col].to_numpy()
    rater2 = df[self_col].to_numpy()

    # Remove NaN values if present
    mask = ~np.isnan(rater1) & ~np.isnan(rater2)
    rater1 = rater1[mask]
    rater2 = rater2[mask]

    # Calculate metrics and append results
    if len(rater1) > 0 and len(rater2) > 0:
        metrics = calculate_metrics(rater1, rater2)
        results.append([f"{conf_col} vs {self_col}"] + metrics)

# Calculate metrics for the entire set (pooled data)
rater1_all = df[conf_monitoring_columns].to_numpy().flatten()
rater2_all = df[self_monitoring_columns].to_numpy().flatten()

# Remove NaN values if present
mask = ~np.isnan(rater1_all) & ~np.isnan(rater2_all)
rater1_all = rater1_all[mask]
rater2_all = rater2_all[mask]

# Calculate metrics and append results for the entire set
if len(rater1_all) > 0 and len(rater2_all) > 0:
    metrics = calculate_metrics(rater1_all, rater2_all)
    results.append(["Entire Set"] + metrics)

# Define headers
headers = [
    "Section", "Cohen's Kappa", "Percentage Agreement (%)", "Number of Observations",
    "True Positive", "False Positive", "False Negative", "True Negative",
    "Total Agreement Count", "Total Observation Count", "Expected Agreement", "P_o - P_e", "1 - P_e", "k"
]

# Create DataFrame and export results to CSV
results_df = pd.DataFrame(results, columns=headers)
output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Save Results CSV")
if output_file_path:
    results_df.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}")
else:
    print("No results to save.")
