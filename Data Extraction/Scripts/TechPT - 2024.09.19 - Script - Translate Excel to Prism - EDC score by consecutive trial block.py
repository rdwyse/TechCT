import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Hide the root window for file dialogs
root = tk.Tk()
root.withdraw()

# Open file dialog to select input CSV file
csv_file = filedialog.askopenfilename(title="Select CSV File",
                                      filetypes=[("CSV Files", "*.csv")])

if csv_file:
    try:
        # Load the CSV data
        df = pd.read_csv(csv_file, parse_dates=['DateTimeStamp'])

        # Ensure required columns are present (without specifying the 'ALL_last_column_value' since it will be dynamic)
        required_columns = ['DateTimeStamp', 'CaregiverID', 'SessionNumber',
                            'TrialBlockGroup', 'StudyPhase', 'All_SessionType']
        if not all(col in df.columns for col in required_columns):
            print("Input CSV file is missing required columns.")
            exit()

        # Get the name of the last column
        last_column = df.columns[-1]

        # Create 'Phase_Part' by combining 'StudyPhase' and 'SessionType'
        def get_phase_part(row):
            study_phase = row['StudyPhase']
            session_type = row['All_SessionType']
            if study_phase == '5_RTB':
                phase_part = 'RTB'
            else:
                phase_part = study_phase.split('_')[-1]
            type_part = session_type.split('_')[-1]
            return f"{phase_part}_{type_part}"

        df['Phase_Part'] = df.apply(get_phase_part, axis=1)

        # Add a row index starting at 1
        df.reset_index(drop=True, inplace=True)
        df['Row_Index'] = df.index + 1

        # Initialize the output DataFrame
        output_df = pd.DataFrame()
        output_df['Trial Block Count'] = df['TrialBlockGroup']

        # Initialize tracking variables
        idx = 0
        column_count = 0
        columns_order = []

        # Main Loop
        while idx < len(df):
            row = df.iloc[idx]
            phase_part1 = row['Phase_Part']
            session_number1 = row['SessionNumber']
            last_column_value1 = row[last_column]  # Use the last column

            # Increment column count
            column_count += 1
            # Create a new column name
            column_name = f"{phase_part1}_{session_number1}_{column_count}"
            # Add the column to output_df
            if column_name not in output_df.columns:
                output_df[column_name] = pd.NA
                columns_order.append(column_name)

            # Place the value from the last column
            output_df.at[idx, column_name] = last_column_value1

            # Nested Loop
            idx += 1
            while idx < len(df):
                row2 = df.iloc[idx]
                phase_part2 = row2['Phase_Part']
                session_number2 = row2['SessionNumber']
                last_column_value2 = row2[last_column]  # Use the last column

                # If phase_part2 == phase_part1 AND session_number2 == session_number1
                if phase_part2 == phase_part1 and session_number2 == session_number1:
                    # Place the value in the same column
                    output_df.at[idx, column_name] = last_column_value2
                    idx += 1
                else:
                    # Break the nested loop and start a new column
                    break

        # Reorder columns
        desired_columns_order = ['Trial Block Count'] + columns_order
        output_df = output_df[desired_columns_order]

        # Open file dialog to save the output CSV file
        output_file = filedialog.asksaveasfilename(defaultextension=".csv",
                                                   filetypes=[("CSV Files", "*.csv")],
                                                   title="Save CSV as")

        if output_file:
            # Export the formatted data to CSV
            output_df.to_csv(output_file, index=False)
            print(f"Data successfully exported to {output_file}")
        else:
            print("Save operation canceled.")

    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("No file selected.")
