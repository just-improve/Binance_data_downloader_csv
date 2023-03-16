from binance.um_futures import UMFutures
from binance.cm_futures import CMFutures
from pprint import pprint

import get_ohlcv
import get_oi
import df_operations
import update_data


class MenuController:
    def __init__(self, model_entry, manager_view):
        self.model_entry = model_entry
        self.manager_view = manager_view
        self.frame = self.manager_view.frames["menu"]
        self._bind()

    def _bind(self):
        self.frame.test_btn.config(command=self.manage_methods)
        self.frame.update_data_btn.config(command=self.update_csv_files_in_directory)

    def manage_methods(self):
        self.store_setting()
        self.choose_proper_method()

    def store_setting(self):
        self.model_entry.mode_data_merge = self.frame.mode_data_merge.get()
        self.model_entry.mode_data_oi = self.frame.mode_data_oi.get()
        self.model_entry.file_name_to_merge = self.frame.file_to_merge_entry.get()
        self.model_entry.symbol = self.frame.symbol_entry.get()
        self.model_entry.pair = self.frame.pair_entry.get()
        self.model_entry.interval = self.frame.interval_entry.get()
        self.model_entry.start_date = self.frame.start_date_entry.get()
        self.model_entry.end_date = self.frame.end_date_entry.get()
        self.model_entry.calculate_final_mode()
        # pprint(vars(self.model_entry))

    def choose_proper_method(self):
        if self.model_entry.final_mode == 'creating_data_ohlcv': # and self.model_entry.mode_data_merge == 0:
            print('creating_data_ohlcv')
            df = get_ohlcv.get_ohlcv_data(self.model_entry.symbol, self.model_entry.pair, self.model_entry.interval,
                                     self.model_entry.start_date, self.model_entry.end_date)
            '''types setting'''
            df_operations.save_df_to_csv(df, self.model_entry.symbol, self.model_entry.pair, self.model_entry.interval)

        elif self.model_entry.final_mode == 'creating_data_oi': #and self.model_entry.mode_data_merge == 0:
            print('creating_data_oi')
            df_ohlcv = get_ohlcv.get_ohlcv_data(self.model_entry.symbol, self.model_entry.pair, self.model_entry.interval,
                                     self.model_entry.start_date, self.model_entry.end_date)

            df_oi = get_oi.get_oi_data(self.model_entry.symbol, self.model_entry.pair,
                                     self.model_entry.start_date, self.model_entry.end_date)
            df_operations.merge_dfs_ovlcv_oi(df_ohlcv, df_oi, self.model_entry.symbol, self.model_entry.pair)
        #
        elif self.model_entry.final_mode == 'merging_data_ohlcv':
            print('merging_data_ohlcv')
            df_read_to_merge = df_operations.read_csv_file(self.model_entry.file_name_to_merge)

            df_ohlcv_created_to_merge = get_ohlcv.get_ohlcv_data(self.model_entry.symbol, self.model_entry.pair,
                                                self.model_entry.interval,
                                                self.model_entry.start_date, self.model_entry.end_date)

            df_operations.merge_two_dataframes_ohlcv(df_ohlcv_created_to_merge, df_read_to_merge,
                                                     self.model_entry.interval, self.model_entry.symbol,
                                                     self.model_entry.pair)
            #
            # print(df_read_to_merge)

        elif self.model_entry.final_mode == 'merging_data_oi':
            print('merging_data_oi')
            df_oi_read_to_merge = df_operations.read_csv_file(self.model_entry.file_name_to_merge)
            df_ohlcv = get_ohlcv.get_ohlcv_data(self.model_entry.symbol, self.model_entry.pair,
                                                self.model_entry.interval,
                                                self.model_entry.start_date, self.model_entry.end_date)

            df_oi = get_oi.get_oi_data(self.model_entry.symbol, self.model_entry.pair,
                                       self.model_entry.start_date, self.model_entry.end_date)
            df_oi_ohlcv = df_operations.get_df_merge_two_dataframes_oi(df_ohlcv, df_oi)
            #
            df_operations.merge_two_dataframes_oi(df_oi_ohlcv, df_oi_read_to_merge, self.model_entry.symbol, self.model_entry.pair)


        # zostało łączenie danych tylko

        # df1['column_name'] = df1['column_name'].astype('float64')
        # merged_df = pd.merge(df1, df2, on='column_name')

        # df_read_to_merge = df_operations.change_ohlcv_column_type(df_read_to_merge)
        # df_read_to_merge = df_read_to_merge.astype('object')

        # df_ohlcv_created_to_merge = df_operations.change_ohlcv_column_type(df_ohlcv_created_to_merge)

        # df_ohlcv_created_to_merge = df_ohlcv_created_to_merge.astype('object')

    def update_csv_files_in_directory(self):
        update_data.get_list_of_csv_files_in_directory()







