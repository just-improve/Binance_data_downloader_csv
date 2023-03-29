
from binance.um_futures import UMFutures
# from binance.cm_futures import CMFutures

def get_tickers_list():
    binance_client_um = UMFutures()
    ticker_price = binance_client_um.ticker_price()
    usdt_only_symbols, usdt_pairs = get_all_usdt_symbols_list(ticker_price)
    print('')
    return usdt_only_symbols, usdt_pairs
def get_all_usdt_symbols_list(all_tickers):
    usdt_only_symbols = []
    usdt_pairs = []

    for symbol_dict in all_tickers:
        for key, value in symbol_dict.items():
            if key == 'symbol':
                if value.endswith('USDT'):
                    usdt_only_symbols.append(value[:len(value)-4])
                    usdt_pairs.append(value)

    return usdt_only_symbols, usdt_pairs