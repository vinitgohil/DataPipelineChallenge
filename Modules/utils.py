from scipy import stats
import numpy as np

# Define function that detects and removes outliers within the dataframe column
def removeOutliers(df, col):
	"""
	This function detects outliers on the dataframe column using the z-score.
	Z-score is a statistical measure that indicates how many deviations a data point ia away from the mean.
	Z-score is calculated using the following method:
	 z = (x - mean) / std

	 x = datapoint
	 mean = mean of the dataset
	 std = standard deviation of the dataset
	:param df: object
	:type df: string
	:param col:
	:type col: string
	:return: dataframe
	:rtype: object
	"""
	z = np.abs(stats.zscore(df[col]))
	# Set threshold value where values are outside 2 of the standard deviation from mean
	threshold = 2
	outliers = df[z > threshold]
	# drop outliers from the dataframe
	df = df.drop(outliers.index)
	return df

if __name__ == "__main__":
    print("Executing the functions")
