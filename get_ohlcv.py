import pandas as pd
from binance.um_futures import UMFutures
from binance.cm_futures import CMFutures

import df_operations

four_day_as_ts = 345600000
two_day_as_ts = 172800000
one_day_as_ts = 86400000
half_day_as_ts = 43200000


def get_ohlcv_data(symbol, pair, interval, start_date, end_date):
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

    # time_substracted = one_day_as_ts   #market_name
    time_substracted = df_operations.calculate_time_substracted(interval)

    start_date = int(1000*(pd.to_datetime(start_date).timestamp()))
    end_date = int(1000*(pd.to_datetime(end_date).timestamp()))
    earlier_date = end_date - time_substracted
    columns = ['TimestampOpen', 'Open', 'High', 'Low', 'Close', 'Volume', 'TimestampClose','Quote_Asset_volume', 'NumberOfTrades', 'TakerBuyVolume', 'Taker buy qav', 'Ignore']
    df = pd.DataFrame(columns=columns)
    last_iteration = False

    while last_iteration is False:

        if start_date > earlier_date:
            earlier_date = start_date
            last_iteration = True
        print(str(pd.to_datetime(earlier_date, unit='ms')) + ' earlier data')
        limit = 1000
        if interval == '5m':
            limit = 500

        if earlier_date < end_date:
            my_kline = binance_client.klines(market_name, interval, startTime=earlier_date,
                                                    endTime=end_date, limit=limit)
            my_kline.reverse()
            new_pd = pd.DataFrame(my_kline, columns=columns)

            df = pd.merge(df, new_pd, how='outer')

        end_date = end_date - time_substracted
        earlier_date = earlier_date - time_substracted

    df['TimestampOpen'] = pd.to_datetime(df['TimestampOpen'], unit='ms')
    df['date'] = df['TimestampOpen'].dt.date
    df['time'] = df['TimestampOpen'].dt.time
    df.drop(['TimestampClose', 'Ignore', 'Quote_Asset_volume', 'Taker buy qav', 'TimestampOpen'], axis='columns',
            inplace=True)
    df['symbol'] = market_name
    new_order = ['symbol', 'date', 'time', 'Open', 'High', 'Low', 'Close', 'Volume', 'NumberOfTrades', 'TakerBuyVolume']
    df = df.reindex(columns=new_order)

    return df



