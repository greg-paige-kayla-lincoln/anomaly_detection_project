def wrangle_df(df):  
    df.set_index('date', inplace=True)
    df.program_id = df.program_id.map({1.0:'full_stack_php', 2.0:'full_stack_java', 3.0:'data_science', 4.0:'front_end_programming'})
    ## drop
    df.drop(columns=['id','slack','deleted_at'],inplace = True)
    date_cols = ['start_date', 'end_date', 'created_at', 'updated_at']
    for col in date_cols: 
        df[col] = pd.to_datetime(df[col])
    return df   