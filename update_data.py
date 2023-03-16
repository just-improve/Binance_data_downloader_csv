import glob
import os


def get_list_of_csv_files_in_directory():
    names_csv_files = glob.glob('my_csv_files/*.csv')
    names_csv_files = [os.path.basename(file) for file in names_csv_files]
    names_csv_files, market_names = extract_market_name_from_names_csv_files(names_csv_files)

    return names_csv_files, market_names


def extract_market_name_from_names_csv_files(names_csv_files):
    market_names = [name.split(' ')[0] for name in names_csv_files]
    return market_names