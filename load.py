import sqlite3
import pandas as pd
import glob


processedFiles = glob.glob("Processed/*.csv")
# load processed data into database
for processedFile in processedFiles:
	# load processed data files
	df = pd.read_csv(processedFile, index_col=None)

	# strip whitespaces from headers
	df.columns = df.columns.str.strip()

	try:
		conn = sqlite3.connect("datapipeline.db")
		# load data into database table
		df.to_sql("turbines", conn, if_exists='append', index=False)
		print(f"data for {processedFile} successfully loaded")
	except Exception as e:
		raise e
	conn.close()

	# sleep(1)

summarisedFiles = glob.glob("Summarised/*.csv")
# load summarised data into database
for summarisedFile in summarisedFiles:

	# load summarised data files
	df = pd.read_csv(summarisedFile, index_col=None)

	# strip whitespaces from headers
	df.columns = df.columns.str.strip()

	try:
		conn = sqlite3.connect("datapipeline.db")

		# load data into test table
		df.to_sql("power_output_summaries", conn, if_exists='append', index=False)
		print(f"data for {summarisedFile} successfully loaded")
	except Exception as e:
		raise e
	conn.close()
