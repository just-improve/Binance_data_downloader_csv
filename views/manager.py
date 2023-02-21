from .menu import MenuView
from .root import Root

class ManagerView:
    def __init__(self):
        self.root = Root()
        self.frames = {}
        self._add_frame(MenuView, "menu")

    def _add_frame(self, Frame, name):
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self):
        self.root.mainloop()
