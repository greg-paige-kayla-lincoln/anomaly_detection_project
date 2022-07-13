import pandas as pd 

def wrangle_df(df):
    
    '''This function takes in a DataFrame of curriculum access logs, does some basic wrangling like 
    mapping program codes to program ID numbers, drops unneeded or duplicated columns, 
    and changes date columns to the datetime data type.'''
    
    #Updates program ID numbers to their respective program titles:
    df.program_id = df.program_id.map({1.0:'full_stack_php', 2.0:'full_stack_java', 3.0:'data_science', 4.0:'front_end_programming'})
    
    ## Drops unneeded or duplicate columns:
    df.drop(columns=['id','slack','deleted_at'],inplace = True)
    
    #Adding a date_time column that combines date and time as strings and converts them to datetime format:
    df['date_time'] = pd.to_datetime(df['date']+ ' ' + df['time'])
    
    #Creates a list of columns containing relevant date data for logs:
    date_cols = ['date', 'start_date', 'end_date', 'created_at', 'updated_at']
    
    #Iterates through list of dates to change them to datetime data type:
    for col in date_cols: 
        df[col] = pd.to_datetime(df[col])
    return df  


def wrangle_lincoln(df):
    
    '''This function takes in a DataFrame of curriculum access logs, does some basic wrangling like 
    mapping program codes to program ID numbers, drops unneeded or duplicated columns, 
    and changes date columns to the datetime data type.'''
    # add date as index
    # this code converts the date time into index
    df["date_time"] = pd.to_datetime(df['date'] + df['time'], format='%Y-%m-%d%H:%M:%S')
    df.set_index('date_time', inplace=True)

    #Updates program ID numbers to their respective program titles:
    df.program_id = df.program_id.map({1.0:'full_stack_php', 2.0:'full_stack_java', 3.0:'data_science', 4.0:'front_end_programming'})
    
    ## Drops unneeded or duplicate columns:
    df.drop(columns=['id','slack','deleted_at','date','time'],inplace = True)
    
    #Creates a list of columns containing relevant date data for logs:
    date_cols = ['start_date', 'end_date', 'created_at', 'updated_at']
    
    #Iterates through list of dates to change them to datetime data type:
    for col in date_cols: 
        df[col] = pd.to_datetime(df[col])
    return df 

#Defining the function that adds the program type column based on program_id:
def program_type(df):
    #Dropping Lines With Null Values:
    df = df.dropna()
    #Creating an empty column on the DataFrame:
    df['program_type'] = pd.Series()
    #Calling type 'web' if program_id is not data_science
    if df.program_id != 'data_science':
        df.program_type ='web'
    #Creating type 'data' if program_id is data:
    elif df.program_id == 'data_science':
        df.program_type = 'data'
    #Returning DataFrame with new program_type column:
    return df