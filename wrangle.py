import pandas as pd

def wrangle_df(df):
    
    '''This function takes in a DataFrame of curriculum access logs, does some basic wrangling like 
    mapping program codes to program ID numbers, drops unneeded or duplicated columns, 
    and changes date columns to the datetime data type.'''
    
    #Updates program ID numbers to their respective program titles:
    df.program_id = df.program_id.map({1.0:'full_stack_php', 2.0:'full_stack_java', 3.0:'data_science', 4.0:'front_end_programming'})
    
    ## Drops unneeded or duplicate columns:
    df.drop(columns=['id','slack','deleted_at'],inplace = True)
    
    #Creates a list of columns containing relevant date data for logs:
    date_cols = ['date','time','start_date', 'end_date', 'created_at', 'updated_at']
    
    #Iterates through list of dates to change them to datetime data type:
    for col in date_cols: 
        df[col] = pd.to_datetime(df[col])
    return df   