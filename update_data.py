import glob
import os
from datetime import date


def get_csv_files_names_and_market_names_in_directory():
    names_csv_files = glob.glob('my_csv_files/*.csv')
    names_csv_files = [os.path.basename(file) for file in names_csv_files]
    market_names = extract_market_name_from_names_csv_files(names_csv_files)

    return names_csv_files, market_names


def extract_market_name_from_names_csv_files(names_csv_files):
    market_names = [name.split(' ')[0] for name in names_csv_files]

    return market_names

def extract_market_name_from_csv_file(csv_file_name):
    market_name = csv_file_name.split(' ')[0][:3]
    # starting_date = csv_file_name.split(' ')[1]
    end_date_csv_file = csv_file_name.split(' ')[2]
    return market_name, end_date_csv_file

def extract_dates_from_csv_file(csv_file_name):
    market_name = csv_file_name.split(' ')[0]
    return market_name

def get_today_date():
    today = date.today().strftime('%Y-%m-%d')
    return today