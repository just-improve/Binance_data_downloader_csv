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












    # binance_client_um
    # 1499040000000,        // Open time
    # "0.01634790",         // Open
    # "0.80000000",         // High
    # "0.01575800",         // Low
    # "0.01577100",         // Close
    # "148976.11427815",    // Volume
    # 1499644799999,        // Close time
    # "2434.19055334",      // Quote asset volume
    # 308,                  // Number of trades
    # "1756.87402397",      // Taker buy base asset volume
    # "28.46694368",        // Taker buy quote asset volume
    # "17928899.62484339"   // Ignore.

    # inverse cm
    # 1591258320000,          // Open time
    # "9640.7",               // Open
    # "9642.4",               // High
    # "9640.6",               // Low
    # "9642.0",               // Close (or latest price)
    # "206",                  // Volume
    # 1591258379999,          // Close time
    # "2.13660389",           // Base asset volume
    # 48,                     // Number of trades
    # "119",                  // Taker buy volume
    # "1.23424865",           // Taker buy base asset volume
    # "0"                     // Ignore.


