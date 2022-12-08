import pandas as pd 

def prepare_store_data(df):
    # convert our date column to datetime type
    df.sale_date= pd.to_datetime(df.sale_date)
    # set index
    df = df.set_index("sale_date").sort_index()
    # adding month column to dataframe(date is in index so must use df.index)
    df['month'] = df.index.month
    # adding day of week to dataframe (date is in index so must use df.index)
    df['day'] = df.index.day_name()
    # create total sales column
    df['sales_total'] = df.sale_amount * df.item_price
    return df 



def prepare_opsd_data(df):
    df.columns = [column.replace('+','_').lower() for column in df]
    # convert our date column to datetime type
    df.date= pd.to_datetime(df.date)
    # set index
    df = df.set_index("date").sort_index()
    # adding year column to dataframe(date is in index so must use df.index)
    df['year'] = df.index.year
    # adding month of week to dataframe (date is in index so must use df.index)
    df['month'] = df.index.month
    # filling zero for nulls 
    df.fillna(0, inplace = True)
    df['wind_solar'] = df.wind + df.solar
    return df 