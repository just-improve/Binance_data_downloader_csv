import pandas as pd
import os

four_day_as_ts = 345600000
two_day_as_ts = 172800000
one_day_as_ts = 86400000
half_day_as_ts = 43200000
thirty_days_as_ts = 2592000000

def save_df_to_csv(df, market_name, pair, interval):
    symbol = market_name + pair
    first_date_row = df['date'].iloc[0]
    last_date_row = df['date'].iloc[-1]
    df.to_csv(f'{symbol} {interval} {last_date_row} {first_date_row}.csv', index=False)

def merge_dfs_ovlcv_oi(df1, df2, market_name, pair):
    '''te dwie metody tutaj użyte wywałały błędy'''
    # df1 = change_ohlcv_column_type(df1)
    # df2 = change_df_oi_column_type(df2)
    symbol = market_name + pair
    df = pd.merge(df1, df2, how='outer')
    print('')
    # df = pd.concat([df1, df2]).drop_duplicates()

    first_date_row = df['date'].iloc[0]
    last_date_row = df['date'].iloc[-1]
    print(last_date_row)
    df.to_csv(f'{symbol} {last_date_row} {first_date_row} oi.csv', index=False)

def merge_two_dataframes_oi(df1, df2, market_name, pair, model_entry_final_mode):
    symbol = market_name + pair
    # df = pd.merge(df1, df2, how='outer')
    df1 = change_df_oi_column_type(df1)
    df2 = change_df_oi_column_type(df2)

    df = pd.concat([df1, df2]).drop_duplicates()

    df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))
    df = df.drop_duplicates(subset=['datetime'])
    df.drop(['datetime'], inplace=True, axis='columns')

    first_date_row = df['date'].iloc[0]
    last_date_row = df['date'].iloc[-1]
    print(last_date_row)
    if model_entry_final_mode == 'merging_data_oi':
        df.to_csv(f'{symbol} {last_date_row} {first_date_row} oi.csv', index=False)

    elif model_entry_final_mode == 'update_merge_group_data_oi':
        file_name = f'{symbol} {last_date_row} {first_date_row} oi.csv'
        file_path = "my_csv_files/{}".format(file_name)
        df.to_csv(file_path, index=False)


def get_df_merge_two_dataframes_oi(df1, df2):
    df = pd.merge(df1, df2, how='outer')

    return df

def merge_two_dataframes_ohlcv(df1, df2, interval, market_name, pair):
    symbol = market_name + pair
    # df = pd.merge(df1, df2, how='outer')
    df = pd.concat([df1, df2]).drop_duplicates()

    df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))
    df = df.drop_duplicates(subset=['datetime'])
    df.drop(['datetime'], inplace=True, axis='columns')

    first_date_row = df['date'].iloc[0]
    last_date_row = df['date'].iloc[-1]
    df.to_csv(f'{symbol} {interval} {last_date_row} {first_date_row}.csv', index=False)

def read_csv_file(file_name):
    df = pd.read_csv(file_name)
    return df


# to nie jest metoda dotycząca df
def calculate_time_substracted(interval):
    time_substracted = one_day_as_ts

    if interval == '1m':
        time_substracted = half_day_as_ts

    elif interval == '3m':
        mnoznik = 2
        time_substracted = one_day_as_ts * mnoznik

    elif interval == '5m':
        # mnoznik = 3
        # time_substracted = one_day_as_ts * mnoznik
        time_substracted = half_day_as_ts

    elif interval == '15m':
        mnoznik = 10
        time_substracted = one_day_as_ts * mnoznik

    return time_substracted

def change_df_column_types(df1, df2):
    df1['Open'] = df1['Open'].astype(int)
    df1['High'] = df1['High'].astype(int)
    df1['Low'] = df1['Low'].astype(int)
    df1['Close'] = df1['Close'].astype(int)
    df1['Volume'] = df1['Volume'].astype(int)
    df1['NumberOfTrades'] = df1['NumberOfTrades'].astype(int)
    df1['TakerBuyVolume'] = df1['TakerBuyVolume'].astype(int)
    df1['sumOpenInterest'] = df1['sumOpenInterest'].astype(int)

    df2['Open'] = df2['Open'].astype(int)
    df2['High'] = df2['High'].astype(int)
    df2['Low'] = df2['Low'].astype(int)
    df2['Close'] = df2['Close'].astype(int)
    df2['Volume'] = df2['Volume'].astype(int)
    df2['NumberOfTrades'] = df2['NumberOfTrades'].astype(int)
    df2['TakerBuyVolume'] = df2['TakerBuyVolume'].astype(int)
    df2['sumOpenInterest'] = df2['sumOpenInterest'].astype(int)
    return df1, df2

def change_df_oi_column_type(df1):
    df1['Open'] = df1['Open'].astype(float)
    df1['High'] = df1['High'].astype(float)
    df1['Low'] = df1['Low'].astype(float)
    df1['Close'] = df1['Close'].astype(float)
    df1['Volume'] = df1['Volume'].astype(float)
    df1['NumberOfTrades'] = df1['NumberOfTrades'].astype(int)
    df1['TakerBuyVolume'] = df1['TakerBuyVolume'].astype(float)
    df1['sumOpenInterest'] = df1['sumOpenInterest'].astype(float)

    return df1

def change_ohlcv_column_type(df1):
    # symbol, date, time, Open, High, Low, Close, Volume, NumberOfTrades, TakerBuyVolume
    df1['Open'] = df1['Open'].astype(float)
    df1['High'] = df1['High'].astype(float)
    df1['Low'] = df1['Low'].astype(float)
    df1['Close'] = df1['Close'].astype(float)
    df1['Volume'] = df1['Volume'].astype(float)
    df1['NumberOfTrades'] = df1['NumberOfTrades'].astype(int)
    df1['TakerBuyVolume'] = df1['TakerBuyVolume'].astype(float)
    return df1

def get_df_commons(df1, df2):
    df_common = pd.merge(df1, df2, on='NumberOfTrades')
    return df_common
    # df1

def remove_csv_old_files(csv_names_in_dir):
    for csv_name in csv_names_in_dir:
        file_path = "my_csv_files/{}".format(csv_name)
        os.remove(file_path)
        print(file_path)


        # os.remove(csv_name)
    # names_csv_files = [os.path.basename(file) for file in csv_names_in_dir]
    # names_csv_files = [os.path.basename(csv_file_name) for csv_file_name in csv_names_in_dir]
    # os.path.basename(csv_file_name)
    # os.remove(csv_names_in_dir)


    # path = 'C:\\Users\\xxx\\PycharmProjects\\Binance Data Downloader Gui\\my_csv_files'
    # path = 'my_csv_files/'

