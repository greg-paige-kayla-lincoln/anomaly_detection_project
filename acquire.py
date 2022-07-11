import pandas as pd 
import os

from env import get_db_url

def get_db_log_data():

    '''If previously-generated CSV of logs exists, returns DataFrame of cached log data. If no CSV exists, 
    accesses Codeup database to pull logs of curriculum access, returns a DataFrame of acquired logs, and caches data in CSV
    format for future use.'''
    filename = "db_log_data.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col = 0)
    else:
        # read the SQL query into a DataFrame
        df = pd.read_sql('''SELECT * FROM logs LEFT JOIN cohorts ON logs.cohort_id = cohorts.id;''', get_db_url('curriculum_logs'))

        # Write that DataFrame to CSV to cache for future use.
        df.to_csv(filename)

    # Return the DataFrame containing the log data:
    return df