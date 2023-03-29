import glob
import os
import delete_today_dates_from_csv_names
from datetime import date


def get_csv_files_names_and_market_names_in_directory_oi():
    names_csv_files = glob.glob('oi_csv_data/*.csv')
    names_csv_files = [os.path.basename(file) for file in names_csv_files]
    names_csv_files = delete_today_dates_from_csv_names.delete_today_dates_oi(names_csv_files)

    return names_csv_files

def get_csv_files_names_and_market_names_in_directory_ohlcv():
    names_csv_files = glob.glob('ohlcv_csv_data/*.csv')
    names_csv_files = [os.path.basename(file) for file in names_csv_files]
    names_csv_files = delete_today_dates_from_csv_names.delete_today_dates_ohlcv(names_csv_files)

    return names_csv_files

def extract_market_name_from_names_csv_files(names_csv_files):
    market_names = [name.split(' ')[0] for name in names_csv_files]

    return market_names

def extract_end_date_from_csv_file(csv_file_name):
    end_date_csv_file = csv_file_name.split(' ')[2]
    return end_date_csv_file

def extract_market_from_csv_file(csv_file_name):
    market_name = csv_file_name.split(' ')[0]
    symbol = ''
    market_pair = ''

    if market_name[len(market_name) - 4:] == 'USDT' or market_name[len(market_name) - 4:] == 'BUSD':
        symbol = market_name[:len(market_name) - 4]
        market_pair = market_name[len(market_name) - 4:]

    if market_name[len(market_name) - 3:] == 'USD' and market_name[len(market_name) - 4:] != 'BUSD':
        symbol = market_name[:len(market_name) - 3]
        market_pair = market_name[len(market_name) - 3:]

    return symbol, market_pair

def extract_pair_from_csv_file(csv_file_name):
    market_name = csv_file_name.split(' ')[0]
    market_name = market_name[:len(market_name)-4]
    return market_name


def extract_interval_from_csv_file(csv_file_name):
    interval = csv_file_name.split(' ')[1]
    return interval


def get_today_date():
    today = date.today().strftime('%Y-%m-%d')
    return today