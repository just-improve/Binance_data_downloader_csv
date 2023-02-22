import pandas as pd

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


def merge_two_dataframes_oi(df1, df2, market_name, pair):
    symbol = market_name + pair
    df = pd.merge(df1, df2, how='outer')
    first_date_row = df['date'].iloc[0]
    last_date_row = df['date'].iloc[-1]
    df.to_csv(f'{symbol} {last_date_row} {first_date_row} oi.csv', index=False)

def get_df_merge_two_dataframes_oi(df1, df2):
    df = pd.merge(df1, df2, how='outer')
    return df

def merge_two_dataframes_ohlcv(df1, df2, interval, market_name, pair):
    symbol = market_name + pair
    df = pd.merge(df1, df2, how='outer')
    first_date_row = df['date'].iloc[0]
    last_date_row = df['date'].iloc[-1]
    df.to_csv(f'{symbol} {interval} {last_date_row} {first_date_row}.csv', index=False)

def read_csv_file(file_name):
    df = pd.read_csv(file_name)
    return df

def convert_colums_to_object(df):
    df['Open'] = df['Open'].astype('object')
    df['High'] = df['High'].astype('object')
    df['Low'] = df['Low'].astype('object')
    df['Close'] = df['Close'].astype('object')
    df['TakerBuyVolume'] = df['TakerBuyVolume'].astype('object')
    df['Volume'] = df['Volume'].astype('object')

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

