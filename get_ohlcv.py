import pandas as pd
from binance.um_futures import UMFutures
from binance.cm_futures import CMFutures

four_day_as_ts = 345600000
two_day_as_ts = 172800000
one_day_as_ts = 86400000
half_day_as_ts = 43200000


def get_ohlcv_data(binance_client_um, symbol, pair, interval, start_date, end_date):

    market_name = symbol+pair
    time_substracted = one_day_as_ts   #market_name
    if interval == '1m':
        mnoznik = 2
        time_substracted = half_day_as_ts

    elif interval == '3m':
        mnoznik = 2
        time_substracted = one_day_as_ts * mnoznik

    elif interval == '5m':
        mnoznik = 3
        time_substracted = one_day_as_ts * mnoznik

    elif interval == '15m':
        mnoznik = 10
        time_substracted = one_day_as_ts * mnoznik

    start_date = int(1000*(pd.to_datetime(start_date).timestamp()))  #'2017-08-16'
    end_date = int(1000*(pd.to_datetime(end_date).timestamp()))      #'2017-08-18'
    print('start date')
    print(start_date)

    print('end_date as timestamp')
    print(end_date)

    earlier_date = end_date - time_substracted

    print(str(pd.to_datetime(start_date, unit='ms')) + ' start date')
    print(str(pd.to_datetime(end_date, unit='ms')) + ' end date ')
    print(str(pd.to_datetime(earlier_date, unit='ms')) + ' earlier data')

    columns = ['TimestampOpen', 'Open', 'High', 'Low', 'Close', 'Volume', 'TimestampClose','Quote_Asset_volume', 'NumberOfTrades', 'TakerBuyVolume', 'Taker buy qav', 'Ignore']
    df = pd.DataFrame(columns=columns)
    last_iteration = False

    while last_iteration is False:

        if start_date > earlier_date:
            earlier_date = start_date
            last_iteration = True
        print(str(pd.to_datetime(earlier_date, unit='ms')) + ' earlier data')
        # print(str(pd.to_datetime(end_date, unit='ms')) + ' end date ')
        # print(end_date)


        if earlier_date < end_date:
            my_kline = binance_client_um.klines(market_name, interval, startTime=earlier_date,
                                                endTime=end_date, limit=1000)
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
    new_order = ['date', 'time', 'Open', 'High', 'Low', 'Close', 'Volume', 'NumberOfTrades', 'TakerBuyVolume']
    df = df.reindex(columns=new_order)

    first_date_row = df['date'].iloc[0]
    last_date_row = df['date'].iloc[-1]
    df.to_csv(f'{market_name} {interval} {last_date_row} {first_date_row} .csv', index=False)


