from tkinter import Frame, Label, Button, Radiobutton, IntVar, Entry

class MenuView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.mode_data_merge = IntVar(self, 0)
        Radiobutton(self, text='Create data', variable=self.mode_data_merge, value=1, command=self.rb_create_merge_listener).grid(row=1, column=0, padx=10, pady=10)
        Radiobutton(self, text='Merge data', variable=self.mode_data_merge, value=0, command=self.rb_create_merge_listener).grid(row=1, column=2, padx=10, pady=10)

        self.mode_data_oi = IntVar(self, 0)

        Radiobutton(self, text='OHLCV', variable=self.mode_data_oi, value=0, command=self.rb_ohlcv_oi_listener).grid(row=2, column=0, padx=10, pady=10)
        Radiobutton(self, text='OHLCV + Oi', variable=self.mode_data_oi, value=1, command=self.rb_ohlcv_oi_listener).grid(row=2, column=2, padx=10, pady=10)

        self.file_to_merge_entry = Entry(self)
        self.file_to_merge_entry.insert(0, 'XRPUSDT 2023-02-16 2023-02-20 oi.csv')  #name file to merge
        self.file_to_merge_entry.grid(row=4, column=2, padx=10, pady=10)
        self.file_to_merge_entry['state'] = 'normal'

        label_symbol = Label(self, text='Symbol')
        label_symbol.grid(row=5, column=0, padx=10, pady=10)

        label_currency = Label(self, text='pair')
        label_currency.grid(row=5, column=2, padx=10, pady=10)

        self.symbol_entry = Entry(self)
        self.symbol_entry.insert(0,'XRP')
        self.symbol_entry.grid(row=6, column=0, padx=10, pady=10)

        self.pair_entry = Entry(self)
        self.pair_entry.insert(0, 'USDT')
        self.pair_entry.grid(row=6, column=2, padx=10, pady=10)

        label_start_date = Label(self, text='Start date')
        label_start_date.grid(row=7, column=0, padx=10, pady=10)

        label_end_date = Label(self, text='End date')
        label_end_date.grid(row=7, column=2, padx=10, pady=10)

        self.start_date_entry = Entry(self)
        self.start_date_entry.insert(0, '2023-02-18')
        self.start_date_entry.grid(row=8, column=0, padx=10, pady=10)

        self.end_date_entry = Entry(self)
        self.end_date_entry.insert(0, '2023-02-23')
        self.end_date_entry.grid(row=8, column=2, padx=10, pady=10)

        label_interval = Label(self, text='Interval')
        label_interval.grid(row=9, column=0, padx=10, pady=10)

        self.interval_entry = Entry(self)
        self.interval_entry.insert(0, '1d')
        self.interval_entry.grid(row=10, column=0, padx=5, pady=5)

        self.test_btn = Button(self, text="Pobierz dane")
        self.test_btn.grid(row=10, column=2, padx=10, pady=10)

        self.update_data_btn = Button(self, text="Update danych")
        self.update_data_btn.grid(row=11, column=2, padx=10, pady=10)

    #teoretycznie to lepiej by było stworzyć metodę na kliknięcie pobierającą do modela aktualny stan  radio buttona

    def rb_ohlcv_oi_listener(self):
        print(self.mode_data_oi.get())
        if self.mode_data_oi.get() == 1:
            self.interval_entry.delete(0, 'end')
            self.interval_entry.insert(0, '5m')
            self.interval_entry['state'] = 'disabled'
        elif self.mode_data_oi.get() == 0:
            self.interval_entry['state'] = 'normal'

            pass  # trzeba zrobić, żeby startową datę sprawdzało i wtedy uzupełniało na maksymalnie 30 dni wstecz i uzupełniało interval na 5m i żeby znikał ten interval


    def rb_create_merge_listener(self):
        if self.mode_data_merge.get() == 0:
            print('zmiana na normalny')
            print(self.mode_data_merge.get())
            self.file_to_merge_entry['state'] = 'normal'
        elif self.mode_data_merge.get() == 1:
            print('zmiana na disabled')
            print(self.mode_data_merge.get())
            self.file_to_merge_entry['state'] = 'disabled'


