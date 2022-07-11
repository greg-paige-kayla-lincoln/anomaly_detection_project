################ Libraries and documents needed for this project ################
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from env import host, user, password

import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split

###################### Acquire and Clean Data ######################
#below are the credentials to the SQL db  linked to a .env file.
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    It takes in a string name of a database as an argument.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
# ----------------------------------------------------------------- #
#the function 
def get_cohort_sql():

    ''' this function calls a sql file from the codeup database and creates a data frame from the curriculum db.     
    '''
    query = '''SELECT * FROM logs   LEFT JOIN  cohorts ON logs.cohort_id = cohorts.id;'''
            

    df = pd.read_sql(query, get_connection('curriculum_logs'))
    #creating a csv for easy access 
    return df


 #this function gets the zillow data thats already saved as a csv file from the zillow data base        
def get_cohort_df():
    '''
    This function reads in curriculum log data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('curriculum.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('curriculum.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = get_cohort_sql()
        
        # Cache data
        df.to_csv('curriculum.csv')
        
    return df

