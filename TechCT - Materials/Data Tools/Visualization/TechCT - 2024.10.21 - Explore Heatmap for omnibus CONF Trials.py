import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Hard-coded file path for the CSV file
input_file_path = r'D:\OneDrive\OneDrive - Central Michigan University\TechCT\TechCT - Public Repository\Public - GitHub - TechCT\TechCT - Materials\Data Tools\Visualization\TechCT - 2024.10.21 - CONF_SC - All Trials - CSV - V1.csv'
# Load the CSV file into a DataFrame
df = pd.read_csv(input_file_path)

# Ensure DateTimeStamp is recognized as a datetime column
df['DateTimeStamp'] = pd.to_datetime(df['DateTimeStamp'])

# Filter data for a specific caregiver (Change 'Case1' to the caregiver you want to visualize)
selected_caregiver = 'Case1'
df_caregiver = df[df['CaregiverID'] == selected_caregiver]

# Reshape the DataFrame for heatmap visualization with each trial, using DateTimeStamp
df_long = pd.melt(df_caregiver, id_vars=['CaregiverID', 'DateTimeStamp'], value_vars=[
    'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4',
    'ConfMonitoring5', 'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3'
], var_name='MonitoringStep', value_name='Performance')

# Convert 'Performance' to binary (assuming it's 0 and 1 for dichotomous data)
df_long['Performance'] = df_long['Performance'].astype(int)

# Organize Monitoring steps as per the custom Y-axis order provided
step_order = [
    'ConfMonitoring1', 'ConfMonitoring2', 'ConfMonitoring3', 'ConfMonitoring4',
    'ConfMonitoring5', 'ConfMonitoring6a_1', 'ConfMonitoring6a_2', 'ConfMonitoring6a_3'
]
y_labels = [
    'Move Close', 'Say Name', 'Task-Specific Feedback', 'Verbal Feedback',
    'Reward Delivery', 'Assertive Delivery', 'Concise Delivery', 'Neutral Delivery'
]

# Reverse the order of the Y-axis to match the desired arrangement
y_labels.reverse()
step_order.reverse()

# Ensure MonitoringStep column follows the correct order
df_long['MonitoringStep'] = pd.Categorical(df_long['MonitoringStep'], categories=step_order, ordered=True)

# Create a pivot table for the heatmap data with individual dates as columns
heatmap_pivot = df_long.pivot_table(index='MonitoringStep', columns='DateTimeStamp', values='Performance')

# Set up the plot (use a binary color palette for dichotomous values)
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_pivot, annot=False, cmap='binary', cbar=False, linewidths=.5, vmin=0, vmax=1)

# Update Y-axis labels with the corrected order
plt.yticks(ticks=[i + 0.5 for i in range(len(y_labels))], labels=y_labels)

# Format X-axis to show date labels clearly with custom date format
plt.xticks(rotation=45, ha='right')
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%a - %m/%d/%y'))

# Remove X and Y axis labels
plt.xlabel("")
plt.ylabel("")

# Show plot
plt.tight_layout()
plt.show()
