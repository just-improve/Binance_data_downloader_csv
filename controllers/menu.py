from binance.um_futures import UMFutures
from binance.cm_futures import CMFutures
from pprint import pprint

import get_ohlcv
import get_oi
import df_operations
import update_data
import tickers_extracter
import os


class MenuController:

    def __init__(self, model_entry, model_update, manager_view):
        self.model_entry = model_entry
        self.model_update = model_update
        self.manager_view = manager_view
        self.frame = self.manager_view.frames["menu"]
        self._bind()
        self.creating_folders_oi_ohlcv()
        # creating folders if doesnt exists

    def _bind(self):
        self.frame.download_btn.config(command=self.manage_methods)
        self.frame.update_data_oi_btn.config(command=self.update_csv_files_in_directory_oi)
        self.frame.update_data_ohlcv.config(command=self.update_csv_files_in_directory_ohlcv)
        self.frame.all_tickers_btn.config(command=self.get_all_tickers)

    def get_all_tickers(self):
        self.model_update.usdt_symbols_only, self.model_update.usdt_pairs = tickers_extracter.get_tickers_list()
        print('')

    def creating_folders_oi_ohlcv(self):

        if not os.path.exists('oi_csv_data'):
            os.makedirs('oi_csv_data')
        if not os.path.exists('ohlcv_csv_data'):
            os.makedirs('ohlcv_csv_data')

    def test_btn_method(self):
        pass
        # df_operations.remove_csv_old_files('BNBUSDT 2023-01-23 2023-03-16 oi.csv')
        # df_operations.remove_csv_old_files(self.model_update.csv_names_in_dir)

    def manage_methods(self):
        self.store_setting()
        self.choose_proper_mode()

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

    def choose_proper_mode(self, csv_name_in_dir=None):
        print(self.model_entry.final_mode)
        if self.model_entry.final_mode == 'creating_data_ohlcv': # and self.model_entry.mode_data_merge == 0:
            print('creating_data_ohlcv')
            df = get_ohlcv.get_ohlcv_data(self.model_entry.symbol, self.model_entry.pair, self.model_entry.interval,
                                     self.model_entry.start_date, self.model_entry.end_date)
            '''types setting'''
            df_operations.save_df_to_csv_ohlcv(df, self.model_entry.symbol, self.model_entry.pair, self.model_entry.interval)

        elif self.model_entry.final_mode == 'creating_data_oi': #and self.model_entry.mode_data_merge == 0:
            print('creating_data_oi')
            df_ohlcv = get_ohlcv.get_ohlcv_data(self.model_entry.symbol, self.model_entry.pair, self.model_entry.interval,
                                     self.model_entry.start_date, self.model_entry.end_date)

            df_oi = get_oi.get_oi_data(self.model_entry.symbol, self.model_entry.pair,
                                     self.model_entry.start_date, self.model_entry.end_date)
            df_operations.merge_dfs_ovlcv_oi(df_ohlcv, df_oi, self.model_entry.symbol, self.model_entry.pair)

        elif self.model_entry.final_mode == 'merging_data_ohlcv':
            print('merging_data_ohlcv')
            df_read_to_merge = df_operations.read_csv_file(self.model_entry.file_name_to_merge)

            df_ohlcv_created_to_merge = get_ohlcv.get_ohlcv_data(self.model_entry.symbol, self.model_entry.pair,
                                                self.model_entry.interval,
                                                self.model_entry.start_date, self.model_entry.end_date)

            df_operations.merge_two_dataframes_ohlcv(df_ohlcv_created_to_merge, df_read_to_merge,
                                                     self.model_entry.interval, self.model_entry.symbol,
                                                     self.model_entry.pair, self.model_entry.final_mode)
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
            df_operations.merge_two_dataframes_oi(df_oi_ohlcv, df_oi_read_to_merge, self.model_entry.symbol,
                                                  self.model_entry.pair, self.model_entry.final_mode)

        elif self.model_entry.final_mode == 'update_merge_group_data_oi':
            file_path = "oi_csv_data/{}".format(csv_name_in_dir)
            df_oi_read_to_merge = df_operations.read_csv_file(file_path)

            df_ohlcv = get_ohlcv.get_ohlcv_data(self.model_entry.symbol, self.model_entry.pair,
                                                self.model_entry.interval,
                                                self.model_entry.start_date, self.model_entry.end_date)

            df_oi = get_oi.get_oi_data(self.model_entry.symbol, self.model_entry.pair,
                                       self.model_entry.start_date, self.model_entry.end_date)
            df_oi_ohlcv = df_operations.get_df_merge_two_dataframes_oi(df_ohlcv, df_oi)
            #
            df_operations.merge_two_dataframes_oi(df_oi_ohlcv, df_oi_read_to_merge, self.model_entry.symbol,
                                                  self.model_entry.pair, self.model_entry.final_mode)

            print('') #update_data_ohlcv

        # należałoby też czytać pair i symbol poprawnie wtedy by było profesjonalnie
        elif self.model_entry.final_mode == 'update_data_ohlcv':
            file_path = "ohlcv_csv_data/{}".format(csv_name_in_dir)
            df_read_to_merge = df_operations.read_csv_file(file_path)
            df_ohlcv_created_to_merge = get_ohlcv.get_ohlcv_data(self.model_entry.symbol, self.model_entry.pair,
                                                                 self.model_entry.interval,
                                                                 self.model_entry.start_date, self.model_entry.end_date)

            df_operations.merge_two_dataframes_ohlcv(df_ohlcv_created_to_merge, df_read_to_merge,
                                                     self.model_entry.interval, self.model_entry.symbol,
                                                     self.model_entry.pair, self.model_entry.final_mode)

    def update_csv_files_in_directory_oi(self):
        self.model_update.csv_names_in_dir = update_data.get_csv_files_names_and_market_names_in_directory_oi()
        self.model_entry.final_mode = 'update_merge_group_data_oi'
        self.model_entry.interval = '5m'
        self.model_entry.end_date = update_data.get_today_date()

        if len(self.model_update.csv_names_in_dir) > 0:
            for csv_name_in_dir in self.model_update.csv_names_in_dir:
                # self.model_entry.symbol, self.model_entry.start_date = \
                #     update_data.extract_market_name_end_date_from_csv_file(csv_name_in_dir)

                self.model_entry.symbol = update_data.extract_market_from_csv_file(csv_name_in_dir)
                self.model_entry.start_date = update_data.extract_end_date_from_csv_file(csv_name_in_dir)
                print('')
                self.choose_proper_mode(csv_name_in_dir)

            df_operations.remove_csv_old_files(self.model_update.csv_names_in_dir)
        else:
            print('no oi data to update')

    def update_csv_files_in_directory_ohlcv(self):
        self.model_update.csv_names_in_dir = update_data.get_csv_files_names_and_market_names_in_directory_ohlcv()
        self.model_entry.final_mode = 'update_data_ohlcv'
        self.model_entry.end_date = update_data.get_today_date()

        if len(self.model_update.csv_names_in_dir) > 0:
            for csv_name_in_dir in self.model_update.csv_names_in_dir:
                # self.model_entry.symbol, self.model_entry.start_date = \
                #     update_data.extract_market_name_end_date_from_csv_file(csv_name_in_dir)

                self.model_entry.symbol = update_data.extract_market_from_csv_file(csv_name_in_dir)
                self.model_entry.start_date = update_data.extract_end_date_from_csv_file(csv_name_in_dir)

                self.model_entry.interval = update_data.extract_interval_from_csv_file(csv_name_in_dir)
                print('')

                self.choose_proper_mode(csv_name_in_dir)
            df_operations.remove_csv_old_files_ohlcv(self.model_update.csv_names_in_dir)
        else:
            print('no csv files to update')







