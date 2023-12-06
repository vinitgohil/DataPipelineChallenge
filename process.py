# Import relevant libraries
import pandas as pd
import glob
from pathlib import Path
from datetime import datetime
from Modules import utils

filepaths = glob.glob("DataFiles/*.csv")
# Import Files from the DataFiles Folder for processing

for filepath in filepaths:
	fileName = Path(filepath).stem
	fileNumber = fileName.split('_')[2]
	currentDateTime = datetime.now().strftime("%Y-%m-%d_%H-%M")

	# Read file into a Pandas Dataframe
	df = pd.read_csv(filepath, header=0)
	# Convert the timestamp column in to datetime object
	df['timestamp'] = pd.to_datetime(df['timestamp'])

	# Clean up dataframe
	# Drop any rows containing Null values from the dataframe
	df = df.dropna()

	# Display the shape of the dataframe before outlier detection and removal
	print("Old Shape: ", df.shape)

	# Call the removeOutlier function to detect and remove outliers from the dataframe
	filtered_df = utils.removeOutliers(df, 'power_output')

	# Display new shape of dataframe after outlier detection and removal.
	print("New Shape: ", filtered_df.shape)

	# Save cleaned files to Processed directory
	print("saving cleaned data...")
	filtered_df.to_csv(f"Processed/processed_data_{fileNumber}_{currentDateTime}.csv",
					   sep=',', encoding='utf-8', header=True, index=None)
	print("saving complete")

	# Calculate the summary statistics for the power_output over same period of 24hrs
	# Define the summaries in the final dataframe to be committed to the database

	# group data by timestamp within 24hrs (1Day) and turbine_id
	grouper = pd.PeriodIndex(filtered_df['timestamp'], freq='D')
	summary_df = filtered_df.groupby([grouper, 'turbine_id']).agg(power_output_mean=('power_output', 'mean'),
																power_ouput_max=('power_output', 'max'),
																power_output_min=('power_output', 'min')).reset_index()

	# write summarised dataframe into csv file
	print("saving summarised data...")
	summary_df.to_csv(f"Summarised/power_summary_{fileNumber}_{currentDateTime}.csv",
					sep=',', encoding='utf-8', header=True, index=None)
	print("summary saving complete")
