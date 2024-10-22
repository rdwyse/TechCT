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

# Define function to filter dataset by study phase and drop specified columns
def filter_and_drop(df, study_phase, drop_columns):
    df_filtered = df[df['StudyPhase'] == study_phase].drop(columns=drop_columns, errors='ignore')
    print(f"Total number of rows in the filtered dataset for {study_phase}: {len(df_filtered)}")
    return df_filtered

# Filter datasets for each study phase
columns_to_drop_1_T1 = ['SelfMonitoring3', 'SelfMonitoring4', 'SelfMonitoring5']
df_1_T1 = filter_and_drop(df, '1_T1', columns_to_drop_1_T1)

columns_to_drop_2_T2 = ['SelfMonitoring1', 'SelfMonitoring2', 'SelfMonitoring6', 'SelfMonitoring6a_1', 'SelfMonitoring6a_2', 'SelfMonitoring6a_3',
                        'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring6', 'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3']
df_2_T2 = filter_and_drop(df, '2_T2', columns_to_drop_2_T2)

columns_to_drop_3_T3 = []
df_3_T3 = filter_and_drop(df, '3_T3', columns_to_drop_3_T3)

# Function to perform kappa calculation on a filtered dataset
def calculate_kappa(df, conf_rater_columns, self_rater_columns):
    # Set specific types for utilized columns
    df = df.astype({col: 'float64' for col in conf_rater_columns + self_rater_columns}, errors='ignore')

    results = []
    for conf_col, self_col in zip(conf_rater_columns, self_rater_columns):
        # Flatten the observations from each pair of columns, ignoring NaNs for calculations
        rater1 = df[conf_col].to_numpy()
        rater2 = df[self_col].to_numpy()

        # Print the number of elements before removing NaNs
        print(f"Number of elements before removing NaNs for {conf_col} and {self_col}: Rater1: {len(rater1)}, Rater2: {len(rater2)}")

        # Remove NaN values if present
        mask = ~np.isnan(rater1) & ~np.isnan(rater2)
        rater1 = rater1[mask]
        rater2 = rater2[mask]

        # Print the number of elements after removing NaNs
        print(f"Number of elements after removing NaNs for {conf_col} and {self_col}: Rater1: {len(rater1)}, Rater2: {len(rater2)}")

        # Check if there are sufficient observations for calculations
        if len(rater1) > 0 and len(rater2) > 0:
            # Calculate Cohen's Kappa for the pair
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
            expected_agreement = ((true_positive + false_negative) / total_observation_count) * ((true_positive + false_positive) / total_observation_count) + ((false_positive + true_negative) / total_observation_count) * ((false_negative + true_negative) / total_observation_count)

            results.append([f"{df['StudyPhase'].iloc[0]} - {conf_col} vs {self_col}", kappa, percent_agreement, num_observations, true_positive, false_positive, false_negative, true_negative, total_agreement_count, total_observation_count, expected_agreement])

            print(f"Cohen's Kappa between {conf_col} and {self_col}: {kappa}")
            print(f"Percentage Agreement between {conf_col} and {self_col}: {percent_agreement:.2f}%")
            print(f"Number of observations between {conf_col} and {self_col}: {num_observations}")
        else:
            print(f"No valid observations available for {conf_col} and {self_col} calculation.")

    return results

# Define monitoring columns for each phase
conf_rater_columns_1_T1 = [col for col in df_1_T1.columns if col.startswith('ConfMonitoring')]
self_rater_columns_1_T1 = [col for col in df_1_T1.columns if col.startswith('SelfMonitoring')]
conf_rater_columns_2_T2 = [col for col in df_2_T2.columns if col.startswith('ConfMonitoring')]
self_rater_columns_2_T2 = [col for col in df_2_T2.columns if col.startswith('SelfMonitoring')]
conf_rater_columns_3_T3 = [col for col in df_3_T3.columns if col.startswith('ConfMonitoring')]
self_rater_columns_3_T3 = [col for col in df_3_T3.columns if col.startswith('SelfMonitoring')]

# Calculate Kappa for each study phase
results_1_T1 = calculate_kappa(df_1_T1, conf_rater_columns_1_T1, self_rater_columns_1_T1)
results_2_T2 = calculate_kappa(df_2_T2, conf_rater_columns_2_T2, self_rater_columns_2_T2)
results_3_T3 = calculate_kappa(df_3_T3, conf_rater_columns_3_T3, self_rater_columns_3_T3)

# Combine all results
results = results_1_T1 + results_2_T2 + results_3_T3

# Calculate Cohen's Kappa for the omnibus set
rater1_all_omnibus = pd.concat([df_1_T1[conf_rater_columns_1_T1], df_2_T2[conf_rater_columns_2_T2], df_3_T3[conf_rater_columns_3_T3]], axis=0).to_numpy().flatten()
rater2_all_omnibus = pd.concat([df_1_T1[self_rater_columns_1_T1], df_2_T2[self_rater_columns_2_T2], df_3_T3[self_rater_columns_3_T3]], axis=0).to_numpy().flatten()

# Remove NaN values if present
mask_omnibus = ~np.isnan(rater1_all_omnibus) & ~np.isnan(rater2_all_omnibus)
rater1_all_omnibus = rater1_all_omnibus[mask_omnibus]
rater2_all_omnibus = rater2_all_omnibus[mask_omnibus]

if len(rater1_all_omnibus) > 0 and len(rater2_all_omnibus) > 0:
    if np.all(rater1_all_omnibus == rater2_all_omnibus):
        kappa = 1.0
        percent_agreement = 100.0
    else:
        kappa = cohen_kappa_score(rater1_all_omnibus, rater2_all_omnibus)
        percent_agreement = np.mean(rater1_all_omnibus == rater2_all_omnibus) * 100
    num_observations = len(rater1_all_omnibus)

    true_positive = np.sum((rater1_all_omnibus == 1) & (rater2_all_omnibus == 1))
    false_positive = np.sum((rater1_all_omnibus == 0) & (rater2_all_omnibus == 1))
    false_negative = np.sum((rater1_all_omnibus == 1) & (rater2_all_omnibus == 0))
    true_negative = np.sum((rater1_all_omnibus == 0) & (rater2_all_omnibus == 0))
    total_agreement_count = true_positive + true_negative
    total_observation_count = len(rater1_all_omnibus)
    expected_agreement = ((true_positive + false_negative) / total_observation_count) * ((true_positive + false_positive) / total_observation_count) + ((false_positive + true_negative) / total_observation_count) * ((false_negative + true_negative) / total_observation_count)

    results.append(["Omnibus - Entire Set", kappa, percent_agreement, num_observations, true_positive, false_positive, false_negative, true_negative, total_agreement_count, total_observation_count, expected_agreement])

    print(f"Cohen's Kappa for the omnibus set: {kappa}")
    print(f"Percentage Agreement for the omnibus set: {percent_agreement:.2f}%")
    print(f"Number of observations for the omnibus set: {num_observations}")
else:
    print("No valid observations available for the omnibus set calculation.")

# Export results to a CSV file
if results:
    results_df = pd.DataFrame(results, columns=["Section", "Cohen's Kappa", "Percentage Agreement (%)", "Number of Observations", "True Positive", "False Positive", "False Negative", "True Negative", "Total Agreement Count", "Total Observation Count", "Expected Agreement"])
    output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Save Results CSV")
    if output_file_path:
        results_df.to_csv(output_file_path, index=False)
        print(f"Results saved to {output_file_path}")
else:
    print("No results to save.")
