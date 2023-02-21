from tkinter import Frame, Label, Button, Radiobutton, IntVar, Entry

class MenuView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.mode_data_merge = IntVar(self, 0)
        self.create_radio_buttons(1, 'Tworzenie danych', 'Łączenie danych', self.mode_data_merge)

        self.mode_data_oi = IntVar(self, 0)
        self.create_radio_buttons(2, 'OHLCV', 'OHLCV + Oi', self.mode_data_oi)

        self.file_to_merge_entry = Entry(self)
        self.file_to_merge_entry.insert(0, 'name file to merge')
        self.file_to_merge_entry.grid(row=4, column=2, padx=10, pady=10)

        label_symbol = Label(self, text='Symbol')
        label_symbol.grid(row=5, column=0, padx=10, pady=10)

        label_currency = Label(self, text='pair')
        label_currency.grid(row=5, column=2, padx=10, pady=10)

        self.symbol_entry = Entry(self)
        self.symbol_entry.insert(0,'BTC')
        self.symbol_entry.grid(row=6, column=0, padx=10, pady=10)

        self.pair_entry = Entry(self)
        self.pair_entry.insert(0, 'USDT')
        self.pair_entry.grid(row=6, column=2, padx=10, pady=10)

        label_start_date = Label(self, text='Start date')
        label_start_date.grid(row=7, column=0, padx=10, pady=10)

        label_end_date = Label(self, text='End date')
        label_end_date.grid(row=7, column=2, padx=10, pady=10)

        self.start_date_entry = Entry(self)
        self.start_date_entry.insert(0, '2023-02-16')
        self.start_date_entry.grid(row=8, column=0, padx=10, pady=10)

        self.end_date_entry = Entry(self)
        self.end_date_entry.insert(0, '2023-02-20')
        self.end_date_entry.grid(row=8, column=2, padx=10, pady=10)

        label_interval = Label(self, text='Interval')
        label_interval.grid(row=9, column=0, padx=10, pady=10)

        self.interval_entry = Entry(self)
        self.interval_entry.insert(0, '5m')
        self.interval_entry.grid(row=10, column=0, padx=5, pady=5)

        self.test_btn = Button(self, text="Pobierz dane")
        self.test_btn.grid(row=10, column=2, padx=10, pady=10)



    def create_radio_buttons(self, row, text1, text2, mode_data):
        values = {text1: 0,
                  text2: 1}
        count = 0
        for (text, value) in values.items():
            Radiobutton(self, text=text, variable=mode_data, value=value).grid(row=row, column=count, padx=10, pady=10)
            count += 2

        #teoretycznie to lepiej by było stworzyć metodę na kliknięcie pobierającą do modela aktualny stan  radio buttona


