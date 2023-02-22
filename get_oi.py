import pandas as pd
from binance.um_futures import UMFutures
from binance.cm_futures import CMFutures

import df_operations

four_day_as_ts = 345600000
two_day_as_ts = 172800000
one_day_as_ts = 86400000
half_day_as_ts = 43200000
thirty_days_as_ts = 2592000000


def get_oi_data(symbol, pair, start_date, end_date):
    interval = '5m'
    binance_client_um = UMFutures()
    binance_client_cm = CMFutures()
    if pair == 'USDT' or pair == 'BUSD':
        market_name = symbol+pair
        binance_client = binance_client_um

    elif pair == 'USD':
        market_name = symbol+pair+'_PERP'
        binance_client = binance_client_cm

    else:
        print('wrong pair')
        return

    time_substracted = df_operations.calculate_time_substracted(interval)

    start_date = int(1000*(pd.to_datetime(start_date).timestamp()))  #'2017-08-16'
    end_date = int(1000*(pd.to_datetime(end_date).timestamp()))      #'2017-08-18'
    earlier_date = end_date - time_substracted
    columns = ['Symbol', 'SumOi', 'SumOiValue', 'Timestamp']
    df = pd.DataFrame(columns=columns)
    last_iteration = False
    count = 0

    while last_iteration is False:

        if start_date > earlier_date:
            earlier_date = start_date
            last_iteration = True


        if earlier_date < end_date:

            oi_hist = binance_client.open_interest_hist(market_name, interval, startTime=earlier_date,
                                                    endTime=end_date, limit=500)
            oi_hist.reverse()
            if count == 0:
                df = pd.DataFrame(oi_hist)
                count += 1
                continue
            new_pd = pd.DataFrame(oi_hist)
            df = pd.merge(df, new_pd, how='outer')

        end_date = end_date - time_substracted
        earlier_date = earlier_date - time_substracted

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    # print(df['timestamp'])
    df['date'] = df['timestamp'].dt.date
    df['time'] = df['timestamp'].dt.time
    df.drop(['sumOpenInterestValue', 'timestamp', 'symbol'], axis='columns',
            inplace=True)
    new_order = ['date', 'time', 'sumOpenInterest']
    df = df.reindex(columns=new_order)
    return df



# def calculate_time_substracted(interval):
#     time_substracted = one_day_as_ts
#
#     if interval == '1m':
#         time_substracted = half_day_as_ts
#
#     elif interval == '3m':
#         mnoznik = 2
#         time_substracted = one_day_as_ts * mnoznik
#
#     elif interval == '5m':
#         # mnoznik = 3
#         # time_substracted = one_day_as_ts * mnoznik
#         time_substracted = half_day_as_ts
#
#     elif interval == '15m':
#         mnoznik = 10
#         time_substracted = one_day_as_ts * mnoznik
#
#     return time_substracted