from controllers.menu import MenuController
from models.model_entry_menu import ModelEntry
from views.manager import ManagerView


class Controller:
    def __init__(self, model_entry: ModelEntry, managerView: ManagerView):
        self.model_entry = model_entry
        self.managerView = managerView
        self.menu_controller = MenuController(model_entry, managerView)

    def start(self):
        self.managerView.start_mainloop()