from binance.um_futures import UMFutures
from binance.cm_futures import CMFutures
from pprint import pprint

import get_ohlcv

class MenuController:
    def __init__(self, model_entry, manager_view):
        self.model_entry = model_entry
        self.manager_view = manager_view
        self.frame = self.manager_view.frames["menu"]
        self._bind()

    def _bind(self):
        self.frame.test_btn.config(command=self.manage_methods)

    def manage_methods(self):
        self.store_setting()

    def store_setting(self):
        self.model_entry.mode_data_merge = self.frame.mode_data_merge.get()
        self.model_entry.mode_data_oi = self.frame.mode_data_oi.get()
        self.model_entry.symbol = self.frame.symbol_entry.get()
        self.model_entry.pair = self.frame.pair_entry.get()
        self.model_entry.interval = self.frame.interval_entry.get()
        self.model_entry.start_date = self.frame.start_date_entry.get()
        self.model_entry.end_date = self.frame.end_date_entry.get()
        self.model_entry.calculate_final_mode()
        # pprint(vars(self.model_entry))

    def get_ovlcv(self):
        binance_client_um = UMFutures()
        get_ohlcv.get_ohlcv_data(binance_client_um, self.model_entry.symbol, self.model_entry.pair, self.model_entry.interval,
                                 self.model_entry.start_date, self.model_entry.end_date)
