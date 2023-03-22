from datetime import date

def delete_today_dates_ohlcv(names_csv_files):
    new_csv_names_list = []
    for csv_file_name in names_csv_files:
        today = date.today().strftime('%Y-%m-%d')
        end_date_csv_file = csv_file_name.split(' ')[3]
        end_date_csv_file = end_date_csv_file[:-4]
        if today != end_date_csv_file:
            new_csv_names_list.append(csv_file_name)
            print('')
    print('')
    return new_csv_names_list

def delete_today_dates_oi(names_csv_files):
    new_csv_names_list = []
    for csv_file_name in names_csv_files:
        today = date.today().strftime('%Y-%m-%d')
        end_date_csv_file = csv_file_name.split(' ')[2]
        if today != end_date_csv_file:
            new_csv_names_list.append(csv_file_name)

    return new_csv_names_list
