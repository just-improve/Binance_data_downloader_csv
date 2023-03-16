
class ModelEntry:
    def __init__(self):
        self.mode_data_merge = -1
        self.mode_data_oi = -1    # 0 pobiera ohlcv   1 pobiera oi
        self.file_name_to_merge = ''
        self.symbol = 'BTC'
        self.pair = 'USDT'
        self.interval = '5m'
        self.start_date = ' '
        self.end_date = ' '
        self.final_mode = 0



    def calculate_final_mode(self):

        if self.mode_data_merge == 1 and self.mode_data_oi == 0:
            print('creating_data_ohlcv model')
            self.final_mode = 'creating_data_ohlcv'

        elif self.mode_data_merge == 1 and self.mode_data_oi == 1:
            print('creating_data_oi model')
            self.final_mode = 'creating_data_oi'

        elif self.mode_data_merge == 0 and self.mode_data_oi == 0:
            print('merging_data_ohlcv model')
            self.final_mode = 'merging_data_ohlcv'

        elif self.mode_data_merge == 0 and self.mode_data_oi == 1:
            print('merging_data_oi model')
            self.final_mode = 'merging_data_oi'

class ModelUpdate:
    def __init__(self):
        self.market_names_in_dir = []
        self.csv_names_in_dir = []