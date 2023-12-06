## Data Pipeline Coding Challenge
This repository contains files that read and process wind turbine files. The turbines
generate power based on wind speed and direction and output measured in megawatts (MW)

The objective is to build a robust scalable program that performs the following:

* __Clean ingested data:__ 
  * Raw data containing any missing/null values and outliers must be removed
* __Calculate Summary Statistics:__
  * Calculate the minimum, maximum and average power output over a 24hr time period
* __Identify Anomalies:__
  * Identify any turbines that have deviated from their expected output power over the same time period.
  * Anomalies here are defined as turbines whose power output is outside of 2 standard deviations from the mean.
* Store the processed and summary stats in the database for further analysis
  * __Please Note:__ Files have been outputted to separate folders for clarity from where they can be loaded  
into the database
  

**Files and Folders**
* __process.py__ 
  - file that processed raw data
  - cleans the data, calls the function to remove outliers
  - saves final processed data into the respective outgoing directories

* __load.py__
  * execution of this file will load the processed and summarised data into the database
  * the data will be appended on a table if it exists (will create new table if it doesn't)

* __DataFiles__
  - stores the raw files for ingestion

* __Processed__
  * Contains the processed files after cleanup and outlier removal

* __Summarised__
  * Contains summarised _power_output_ data files after raw data has been processed

* __Modules__
  * contains the _utils.py_ that contains the function for outlier detection and removal.
