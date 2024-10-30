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

# Define function to filter dataset by caregiver case
def filter_dataset(df, caregiver_id, study_phase):
    df_filtered = df[(df['CaregiverID'] == caregiver_id) & (df['StudyPhase'] == study_phase)]
    print(f"Total number of rows in the filtered dataset for {caregiver_id}, {study_phase}: {len(df_filtered)}")
    return df_filtered

# Filter datasets for each case and phase
df_case1_t1 = filter_dataset(df, 'Case1', '1_T1')
df_case1_t2 = filter_dataset(df, 'Case1', '2_T2')
df_case1_t3 = filter_dataset(df, 'Case1', '3_T3')
df_case2_t1 = filter_dataset(df, 'Case2', '1_T1')
df_case2_t2 = filter_dataset(df, 'Case2', '2_T2')
df_case2_t3 = filter_dataset(df, 'Case2', '3_T3')
df_case3_t1 = filter_dataset(df, 'Case3', '1_T1')
df_case3_t2 = filter_dataset(df, 'Case3', '2_T2')
df_case3_t3 = filter_dataset(df, 'Case3', '3_T3')

# Function to perform kappa calculation on a filtered dataset
def calculate_kappa(df, conf_rater_columns, self_rater_columns, case_label):
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
            p_o_minus_p_e = percent_agreement / 100 - expected_agreement
            one_minus_p_e = 1 - expected_agreement
            k = p_o_minus_p_e / one_minus_p_e if one_minus_p_e != 0 else np.nan

            results.append([f"{case_label} - {conf_col} vs {self_col}", kappa, percent_agreement, num_observations, true_positive, false_positive, false_negative, true_negative, total_agreement_count, total_observation_count, expected_agreement, p_o_minus_p_e, one_minus_p_e, k])

            print(f"Cohen's Kappa between {conf_col} and {self_col}: {kappa}")
            print(f"Percentage Agreement between {conf_col} and {self_col}: {percent_agreement:.2f}%")
            print(f"Number of observations between {conf_col} and {self_col}: {num_observations}")
        else:
            print(f"No valid observations available for {conf_col} and {self_col} calculation.")

    return results

# Define monitoring columns for each case and phase
conf_rater_columns = [col for col in df.columns if col.startswith('ConfMonitoring')]
self_rater_columns = [col for col in df.columns if col.startswith('SelfMonitoring')]

# Pool datasets for each case across all phases (T1, T2, T3)
df_case1_pooled = pd.concat([df_case1_t1, df_case1_t2, df_case1_t3], ignore_index=True)
df_case2_pooled = pd.concat([df_case2_t1, df_case2_t2, df_case2_t3], ignore_index=True)
df_case3_pooled = pd.concat([df_case3_t1, df_case3_t2, df_case3_t3], ignore_index=True)

# Now perform the kappa calculation on the pooled data for each case
results_case1_pooled = calculate_kappa(df_case1_pooled, conf_rater_columns, self_rater_columns, 'CaregiverID Case1, Pooled Agreement')
results_case2_pooled = calculate_kappa(df_case2_pooled, conf_rater_columns, self_rater_columns, 'CaregiverID Case2, Pooled Agreement')
results_case3_pooled = calculate_kappa(df_case3_pooled, conf_rater_columns, self_rater_columns, 'CaregiverID Case3, Pooled Agreement')

# Combine all pooled results
results_pooled = results_case1_pooled + results_case2_pooled + results_case3_pooled  # + results_case4_pooled if Case4 is applicable

# Export the pooled results to a CSV file
if results_pooled:
    results_df_pooled = pd.DataFrame(results_pooled, columns=["Section", "Cohen's Kappa", "Percentage Agreement (%)", "Number of Observations", "True Positive", "False Positive", "False Negative", "True Negative", "Total Agreement Count", "Total Observation Count", "Expected Agreement", "P_o - P_e", "1 - P_e", "k"])
    output_file_path_pooled = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Save Pooled Results CSV")
    if output_file_path_pooled:
        results_df_pooled.to_csv(output_file_path_pooled, index=False)
        print(f"Pooled results saved to {output_file_path_pooled}")
else:
    print("No pooled results to save.")
