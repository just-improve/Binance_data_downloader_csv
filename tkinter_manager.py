import tkinter as tk


def open_new_window(usdt_pairs_list, root):
    new_window = tk.Toplevel(root)
    new_window.title("Nowe Okno")
    usdt_pairs_formatted = format_list_of_usdt_pairs(usdt_pairs_list)
    new_label = tk.Label(new_window, text=usdt_pairs_formatted)
    new_label.pack()

def format_list_of_usdt_pairs(usdt_pairs_list):
    usdt_pairs = ''
    count = 0
    for usdt_pair in usdt_pairs_list:
        if count == 6:
            usdt_pairs += usdt_pair + '\n'
            count = 0
        else:
            usdt_pairs += usdt_pair + "   "
            count += 1


    return usdt_pairs