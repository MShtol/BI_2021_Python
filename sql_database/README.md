# Database construction with SQL
In this script you can find construction of SQL-database from specific .xlsx file (thw one in directoru :) ) and a couple of functions for working with it.

Original Data contains 33 columns of usefull info:
- 3first rows - ID in original DB, Sequence itself and its length.
- 30 popular features of interest for AMP, with value=1 if such property was described for particular AMP, otherwise value=0

## Functions
- excel_to_sql(excel_path, db_path, table_name) - This function creates database from .xlsx file containing AMP ID, Sequence, Length and 30 features for each AMP.
- add_amp(amp, db_path, table_name) - This function adds one new AMP to the database.As `amp` is used Amp object
- del_amp(adaptable_ID, db_path, table_name) - This function deletes ine AMP from the database by adaptable_ID value
- select_len(db_path, table_name, start=10, end=50) - This function selects from the DB rows with Length value between `start` and `end`. Returns dataframe with selected rows
- select_by_features(db_path, table_name, features) - This function selects from the DB rows that posses requiered features. Features can be passed as list of column names (except IDs, Sequence and Length). Returns dataframe with selected rows

## Classes
- Amp -This class creates AMP object. It looks usefull because of sparcity of data for each AMP. E.g. ypu can find papers with a number of peptides with only couple of this features been tested.

## Requirements

You can find them in requierements.txt and install with `pip install -r requirements.txt` in your terminal
