from tkinter import Frame, Label, Button


class MenuView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Home")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.test_btn = Button(self, text="Print")
        self.test_btn.grid(row=2, column=0, padx=10, pady=10)


